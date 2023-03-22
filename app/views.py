from django.shortcuts import render
import requests, json

# mudar de lugar depois
def getCityWeather(city):
  apiKey = "a064781f48c41b68062dde044abf4d83"
  response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={apiKey}").json()
  return response

# Create your views here.
def index(request):
  weather = {
    "city": "Fortaleza",
    "temp": 36,
    "tempMin": 34,
    "tempMax": 40,
    "humidity": 40,
    "pressure": 15
  }
  context = { "weather": weather }
  return render(request, "app/index.html", context)