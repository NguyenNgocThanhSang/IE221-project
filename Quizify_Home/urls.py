from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home_login, name='home_login'),
]
