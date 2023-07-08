from django.shortcuts import render
from .pgn_translator import translate_pgn_game

# Create your views here.

def index(request):
    translated_game = None

    if request.method == 'POST':
        game = request.POST.get('text')
        source_language = "en"
        target_language = "es"
        translated_game = translate_pgn_game(source_language, target_language, game)

    return render(request, 'translator/index.html', {'translated_game': translated_game})
