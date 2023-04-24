from django.urls import path
from . import views

urlpatterns = [
  path("", views.redirect, name="redirect"),
  path("<str:city>/", views.index, name="index"),
  path("request/delete/", views.deleteRequests, name="deleteRequests"),
  path("request/get/", views.getRequests, name="geyRequests")
]