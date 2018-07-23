from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_create(request):
    pass

def post_detail(request):
    pass

def post_list(request):
    return render(request, 'index.html')

def post_update(request):
    pass

def post_delete(request):
    pass
