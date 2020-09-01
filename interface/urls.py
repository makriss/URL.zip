
from django.contrib import admin
from django.urls import path, re_path

from interface import views

urlpatterns = [
    path('', views.show_homepage, name="homepage"),
    re_path(r'^(?P<hashed_url>[0-9a-zA-Z]{1,15})$', views.resolve_and_redirect)
]