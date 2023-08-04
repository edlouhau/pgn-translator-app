"""Defines URL patterns for translator."""
from django.urls import path
from translator.views import index

app_name = 'translator'
urlpatterns = [
    # Home page
    path('', index, name='translated_game'),
]
