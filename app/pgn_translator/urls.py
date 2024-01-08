"""Defines URL patterns for translator."""
from django.urls import path
from app.pgn_translator.views import index
from . import views

app_name = 'pgn_translator'
urlpatterns = [
    # Home page
    path('', index, name='translated_game'),
    path("about/", views.about, name="about"),
]
