
from django.contrib import admin
from django.urls import path

from zipper import views

urlpatterns = [
    path('<str:url>', views.minify_url)
]