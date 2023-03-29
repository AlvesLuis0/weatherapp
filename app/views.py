from django.shortcuts import render
from .functions.weather import *

# Create your views here.
def index(request, city):
  response = responseCleaner(getCityWeather(city))
  context = {}

  if(response):
    context = { "weather": response }

  return render(request, "app/index.html", context)