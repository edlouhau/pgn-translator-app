from django import forms
class GameForm(forms.Form):
    game = forms.CharField(widget=forms.Textarea(attrs={"rows": 15, "cols": 75, 'placeholder': 'Paste PGN'}), label= '', required=False)
class TranslatedGame(forms.Form):
      translated_pgn = forms.CharField(widget=forms.Textarea(attrs={"rows": 15, "cols": 75, 'placeholder': 'foo','readonly':'readonly'}), label= '', required=False)
