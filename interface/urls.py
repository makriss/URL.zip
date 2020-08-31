
from django.contrib import admin
from django.urls import path

from interface import views

urlpatterns = [
    path('', views.show_homepage, name="homepage")
]