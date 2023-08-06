from django import forms

LANGUAGE_CHOICES = [
    ("en", "English"),    # English
    ("es", "Spanish"),    # Spanish
    ("cs", "Czech"),      # Czech
    ("da", "Danish"),     # Danish
    ("nl", "Dutch"),      # Dutch
    ("et", "Estonian"),   # Estonian
    ("fi", "Finnish"),    # Finnish
    ("fr", "French"),     # French
    ("de", "German"),     # German
    ("he", "Hungarian"),  # Hungarian
    ("is", "Icelandic"),  # Icelandic
    ("it", "Italian"),    # Italian
    ("no", "Norwegian"),  # Norwegian
    ("pl", "Polish"),     # Polish
    ("pt", "Portuguese"), # Portuguese
    ("ro", "Romanian"),   # Romanian
    ("sv", "Swedish"),  # Swedish
]

class GameForm(forms.Form):
    lang_choices = forms.CharField(label=False, widget=forms.Select(choices=LANGUAGE_CHOICES,attrs={'class': 'mb-4 shadow-sm dropdown btn btn-outline-secondary'}), required=False)
    game = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 75, 'placeholder': 'Paste PGN','class': 'form-control shadow'}), label= '', required=False)
class TranslatedGame(forms.Form):
      lang_choices = forms.CharField(label=False, widget=forms.Select(choices=LANGUAGE_CHOICES,attrs={'class': 'mb-4 shadow-sm dropdown btn btn-outline-secondary'}), required=False)
      translated_pgn = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 75, 'readonly':'readonly','class': 'form-control shadow'}), label=False, required=False)
      
