
from django.contrib import admin
from django.urls import path

from zipper import views

urlpatterns = [
    path('', views.minify_url),
    path('count/', views.get_shortening_count)
]