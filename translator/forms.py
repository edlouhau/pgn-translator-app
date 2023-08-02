from django import forms

class GameForm(forms.Form):
    def __init__(self, *args, **kwargs):
        your_variable = kwargs.pop('your_form_field', None)
        super(GameForm, self).__init__(*args, **kwargs)

        if your_variable:
            self.fields['your_form_field'].initial = your_variable
    
    game = forms.CharField(widget=forms.Textarea(attrs={"rows": 20, "cols": 75, 'placeholder': 'Paste PGN'}), label= '')

    translated_pgn = forms.CharField(widget=forms.Textarea(attrs={"rows": 20, "cols": 75, 'placeholder': "foo"}), label= '')
    
   
