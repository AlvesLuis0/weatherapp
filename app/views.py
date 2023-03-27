from django.shortcuts import render
from datetime import datetime
import requests

# mudar de lugar depois
def getCityWeather(city):
  apiKey = "a064781f48c41b68062dde044abf4d83"
  response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={apiKey}").json()
  return response

def responseCleaner(response):
  if(response["cod"] != 200):
    return False

  date = datetime.now()

  return {
    "city": response["name"],
    "country": response["sys"]["country"],
    "month": date.strftime("%B"),
    "day": date.day,
    "year": date.year,
    "weekDay": date.strftime("%A"),
    "icon": response["weather"][0]["icon"],
    "main": response["weather"][0]["main"],
    "description": response["weather"][0]["description"],
    "temp": response["main"]["temp"],
    "tempMin": response["main"]["temp_min"],
    "tempMax": response["main"]["temp_max"]
  }

# Create your views here.
def index(request, city):
  response = responseCleaner(getCityWeather(city))
  context = {}

  if(response):
    context = { "weather": response }

  return render(request, "app/index.html", context)