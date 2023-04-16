"""Defines URL patterns for translator."""
from django.urls import path
from . import views
app_name = 'translator'
urlpatterns = [
# Home page
path('', views.index, name='index'),
]