from django.urls import path
from ChatApp import views

urlpatterns = [
    path("", views.home, name="home"),
]