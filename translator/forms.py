from django import forms
class GameForm(forms.Form):
    game = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 75, 'placeholder': 'Paste PGN','class': 'form-control'}), label= '', required=False)
class TranslatedGame(forms.Form):
      translated_pgn = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 75, 'readonly':'readonly','class': 'form-control'}), label= '', required=False)
