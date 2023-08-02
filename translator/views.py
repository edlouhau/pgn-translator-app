from django.shortcuts import render
from .pgn_translator import translate_pgn_game
from .forms import GameForm


# Create your views here.

# Refactored Django Form.

def index(request):
    your_variable = "Some value"  # This is the variable you want to pass to the form
    form = GameForm(initial={'your_form_field': your_variable})
    
    source_lang_option = request.POST.get('source_option')
    target_lang_option = request.POST.get('target_option')
    
    global translated_game
    translated_game = ""
    game = ""

    if request.method == "POST":
        game = GameForm(request.POST.get('game'))

        if game.is_valid():

            source_language = "en"
            target_language = "es"

            
            translated_game = translate_pgn_game(source_language, target_language, game)
            
            context = {'translated_game': translated_game, 'game': game}

        return render(request, 'translator/index.html', context)

    else:
        form = GameForm()

    return render(request, 'translator/index.html', {"form": form})

# End Refactored Django Form.



# def index(request):
#     source_lang_option  = request.POST.get('source_option')
#     target_lang_option = request.POST.get('target_option')

#     translated_game = None
#     game = ""

#     if request.method == 'POST':
#         game = request.POST.get('game')

#         # source_language = source_lang_option
#         # target_language = target_lang_option

#         source_language = "en"
#         target_language = "es"


#         translated_game = translate_pgn_game(source_language, target_language, game)
#     return render(request, 'translator/index.html', {'translated_game': translated_game, 'game': game})


# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/thanks/")

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'translator/index.html', {"form": form})
