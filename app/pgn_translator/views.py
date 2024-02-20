from typing import IO
from django.shortcuts import render
from app.pgn_translator.translate_pgn import translate_pgn_game, translate_tags_comments
from .forms import GameForm,TranslatedGame, TranslationMenuForm, UploadPgnForm

def write_to_disk(file_upload_stream: IO[str]) -> None:
    """
    Writes an IO stream to file on disk

    Args:
        file_upload_stream (IO[str]): The file to write to disk
    """
    with open('app/pgn_translator/uploads/'+file_upload_stream.name, 'wb+') as destination:
        for chunk in file_upload_stream.chunks():
            destination.write(chunk)

def read_from_disk(file: IO[str]) -> str:
    """
    Loads a string from a file on disk

    Args:
        file (IO[str]): The file to read from disk

    Returns:
        str: The content of the file
    """
    with open('app/pgn_translator/uploads/'+file.name, 'r') as file:
        content = file.read()
        return content

def handle_uploaded_file(f):
    write_to_disk(f)
    content = read_from_disk(f)
    return content


def index(request):
    context = {}

    if request.method == "POST":
        
        input_pgn_file_form = UploadPgnForm(request.POST,request.FILES)
        if input_pgn_file_form.is_valid(): 
            pgn_content= handle_uploaded_file(request.FILES["upload_pgn_file"])
            context['file_content'] = pgn_content 
            game = pgn_content

        source_lang_form = GameForm(request.POST)
        target_lang_form = TranslatedGame(request.POST)
        
        if source_lang_form.is_valid() and target_lang_form.is_valid():
            game = source_lang_form.cleaned_data['game']
            source_language = source_lang_form.cleaned_data['game_form_source_lang_choices']
            target_language = target_lang_form.cleaned_data['translated_game_target_lang_choices']
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

    context.update({'source_form': source_lang_form,
                   'target_form': target_lang_form })
    return render(request, 'pgn_translator/index.html', context)


def file_upload(request):
    context = {}

    if request.method == "POST":
        
        input_pgn_file_form = UploadPgnForm(request.POST,request.FILES)
        if input_pgn_file_form.is_valid(): 
            pgn_content= handle_uploaded_file(request.FILES["upload_pgn_file"])
            context['file_content'] = pgn_content 
            game = pgn_content

        source_lang_form = TranslationMenuForm(request.POST)
        target_lang_form = TranslationMenuForm(request.POST)
        
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
        
        input_pgn_file_form = UploadPgnForm()
        source_lang_form = TranslationMenuForm()
        target_lang_form = TranslationMenuForm()

    context.update({'input_pgn_file': input_pgn_file_form, 'source_form': source_lang_form, 'target_form': target_lang_form})
    return render(request, 'pgn_translator/file_upload.html', context)

def about(request):
    return render(request, "pgn_translator/about.html")


