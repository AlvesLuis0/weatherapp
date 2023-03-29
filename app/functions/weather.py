from datetime import datetime
import requests

# requisitando detalhes do clima da cidade passada como parâmetro
def getCityWeather(city):
  apiKey = "a064781f48c41b68062dde044abf4d83"
  response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={apiKey}").json()
  return response

# limpando a resposta, obtendo apenas o necessário
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