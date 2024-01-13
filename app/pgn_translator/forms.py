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
    ("hu", "Hungarian"),  # Hungarian
    ("is", "Icelandic"),  # Icelandic
    ("it", "Italian"),    # Italian
    ("no", "Norwegian"),  # Norwegian
    ("pl", "Polish"),     # Polish
    ("pt", "Portuguese"), # Portuguese
    ("ro", "Romanian"),   # Romanian
    ("sv", "Swedish"),    # Swedish
]

GAMES_LIST = [
    ("Game 1", "Game 1"),
    ("Game 2", "Game 2"),
    ("Game 3", "Game 3"),
]

class UploadPgnForm(forms.Form):
    upload_pgn_file = forms.FileField()

class GameForm(forms.Form):
    source_lang_choices = forms.CharField(label='', widget=forms.Select(choices=LANGUAGE_CHOICES, attrs={
                                          'class': 'mb-4 shadow-sm dropdown btn btn-outline-secondary'}), required=False)
    game = forms.CharField(widget=forms.Textarea(attrs={
                           "rows": 10, "cols": 75, 'placeholder': 'Paste PGN', 'class': 'form-control shadow'}), label='', required=False)

# Swap languages at index 0 and 1.
LANGUAGE_CHOICES[0], LANGUAGE_CHOICES[1] = LANGUAGE_CHOICES[1], LANGUAGE_CHOICES[0]

class TranslatedGame(forms.Form):
    target_lang_choices = forms.CharField(label='', widget=forms.Select(choices=LANGUAGE_CHOICES, attrs={
                                          'class': 'mb-4 shadow-sm dropdown btn btn-outline-secondary'}), required=False)
    translated_pgn = forms.CharField(widget=forms.Textarea(
        attrs={"rows": 10, "cols": 75, 'readonly': 'readonly', 'class': 'form-control shadow'}), label='', required=False)
