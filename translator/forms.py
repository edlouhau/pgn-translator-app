from django import forms

LANGUAGE_CHOICES = [
    ("en", "English"),
    ("es", "Spanish"),
]

class GameForm(forms.Form):
    lang_choices = forms.CharField(label=False, widget=forms.Select(choices=LANGUAGE_CHOICES), required=False)
    game = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 75, 'placeholder': 'Paste PGN','class': 'form-control'}), label= '', required=False)
class TranslatedGame(forms.Form):
      lang_choices = forms.CharField(label=False, widget=forms.Select(choices=LANGUAGE_CHOICES), required=False)
      translated_pgn = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 75, 'readonly':'readonly','class': 'form-control'}), label=False, required=False)
      
