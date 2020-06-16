from django import forms
from .models import Botschaft

class Msg_form(forms.Form):
    msg = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'autocomplete':'off'}))
    class Meta:
        model= Botschaft
