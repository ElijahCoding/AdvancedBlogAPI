import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'
    city = 'Las Vegas'

    res = requests.get(url.format(city)).json()

    city_weather = {
        'city' : city,
        'temperature': res['main']['temp'],
        'description': res['weather'][0]['description'],
        'icon': res['weather'][0]['icon']
    }

    context = { 'city_weather': city_weather }

    return render(request, 'weather/weather.html', context)
