# This file will hold the mapping of urls to views
# It will be imported my the master urls.py (../ac_helper/urls.py)

from django.urls import path

# Import the views.py
from . import views

urlpatterns = [
  path('', views.all, name='index'), # Index page,
  path('all', views.all, name='all'), # List all page
  path('month/<slug:month_name>/', views.month, name='month'), # Monthly highlights page
  path('art', views.art, name='art'), # Artwork (fake checking) page
  path('flowers', views.flowers, name='flowers'), # Flower and hybrid page
]