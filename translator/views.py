from django.shortcuts import render
from .pgn_translator import translate_pgn_game
from .forms import GameForm
from .forms import TranslatedGame

# Create your views here.

def index(request):
    context = {}
    
    if request.method == "POST":
        source_lang_form = GameForm(request.POST)
        target_lang_form = TranslatedGame(request.POST)
        
        if source_lang_form.is_valid() and target_lang_form.is_valid():
            game = source_lang_form.cleaned_data['game']
            source_language = source_lang_form.cleaned_data['source_lang_choices']
            target_language = target_lang_form.cleaned_data['target_lang_choices']
            translated_game = translate_pgn_game(source_language, target_language, game)
            target_lang_form = TranslatedGame(initial={'target_lang_choices': target_language, 'translated_pgn': translated_game})
            context['translated_game'] = translated_game
            print('The request method is:', request.method) #TODO Remove print statements.
            print('The POST data is:', request.POST)
            print('Source_language', source_language)
            print('Target_language', target_language)
            
    else:
        source_lang_form = GameForm()
        target_lang_form = TranslatedGame()
    
    context.update({'source_form': source_lang_form, 'target_form': target_lang_form})
    return render(request, 'translator/index.html', context)



