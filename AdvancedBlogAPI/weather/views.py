import requests
from django.shortcuts import render
from .models import City

# Create your views here.
def index(request):
    url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'
    city = 'Las Vegas'

    weather_data = []
    
    cities = City.objects.all()

    for city in cities:
        res = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature': res['main']['temp'],
            'description': res['weather'][0]['description'],
            'icon': res['weather'][0]['icon']
        }

        weather_data.append(city_weather)

    context = { 'weather_data': weather_data }

    return render(request, 'weather/weather.html', context)
