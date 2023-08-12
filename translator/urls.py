"""Defines URL patterns for translator."""
from django.urls import path
from translator.views import index
from . import views

app_name = 'translator'
urlpatterns = [
    # Home page
    path('', index, name='translated_game'),
    path("about/", views.about, name="about"),
]
