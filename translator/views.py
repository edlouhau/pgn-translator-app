from django.shortcuts import render

# Create your views here.

def index(request):
    translated_game = None

    if request.method == 'POST':
        game = request.POST.get('text')
        translated_game = game.upper()

    return render(request, 'translator/index.html', {'translated_game': translated_game})
