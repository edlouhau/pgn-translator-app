"""Defines URL patterns for translator."""
from django.urls import path
from translator.views import index, get_name

app_name = 'translator'
urlpatterns = [
    # Home page
    path('', index, name='translated_game'),
    path('', get_name, name='name_form')
]
