from django import forms

class SentimentForm(forms.Form):
    text = forms.CharField(max_length=500, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter text to analyze',
        'class': 'form-control'
    }))
