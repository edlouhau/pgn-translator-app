from django.shortcuts import render
from app.pgn_translator.translate_pgn import translate_pgn_game, translate_tags_comments
from .forms import GameForm
from .forms import TranslatedGame
from .forms import UploadPgnForm

def handle_uploaded_file(f):   
    with open('pgn-translator/uploads/'+f.name, 'wb+') as destination:   
        for game in f.games(): 
            destination.write(game) 

def index(request):
    context = {}

    if request.method == "POST":
        
        input_pgn_file_form = UploadPgnForm(request.POST,request.FILES)
        if input_pgn_file_form.is_valid(): 
            handle_uploaded_file(request.FILES["upload_pgn_file"]) 
        
        source_lang_form = GameForm(request.POST)
        target_lang_form = TranslatedGame(request.POST)
        
        if source_lang_form.is_valid() and target_lang_form.is_valid():
            game = source_lang_form.cleaned_data['game']
            source_language = source_lang_form.cleaned_data['source_lang_choices']
            target_language = target_lang_form.cleaned_data['target_lang_choices']
            translated_pgn_moves = translate_pgn_game(
                source_language, target_language, game)

            # Translate game comments.
            translated_game = translate_tags_comments(
                source_language, target_language, translated_pgn_moves)

            target_lang_form = TranslatedGame(
                initial={'target_lang_choices': target_language, 'translated_pgn': translated_game})
            context['translated_game'] = translated_game

    else:
        source_lang_form = GameForm()
        target_lang_form = TranslatedGame()
        input_pgn_file_form = UploadPgnForm()

    context.update({'source_form': source_lang_form,
                   'target_form': target_lang_form,'input_pgn_file': input_pgn_file_form })
    return render(request, 'pgn_translator/index.html', context)

def about(request):
    return render(request, "pgn_translator/about.html")

