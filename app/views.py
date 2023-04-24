from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from .functions.weather import *
from .models import REQUEST

# Create your views here.
def index(request, city):
  response = responseCleaner(getCityWeather(city))
  context = {}

  if(response):
    context = { "weather": response }
    REQUEST.objects.create(
      CITY = response["city"],
      DATE = timezone.now()
    )

  return render(request, "index.html", context)

def deleteRequests(request):
  REQUEST.objects.all().delete()
  return HttpResponse("<h1>Done</h1>")

def getRequests(request):
  context = { "requests": REQUEST.objects.order_by("-DATE")[:11] }
  return render(request, "table.html", context)

def redirect(request):
  return HttpResponseRedirect("Fortaleza/")