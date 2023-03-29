from django.urls import path
from . import views

urlpatterns = [
  path("<str:city>", views.index, name="index"),
  path("request/delete/", views.deleteRequests, name="deleteRequests")
]