from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for the translator."""
    return render(request, 'translator/index.html')
