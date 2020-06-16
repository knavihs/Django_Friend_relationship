from django import forms
from .models import People,Posts

class login_form(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput,max_length=10)
    class Meta:
        model = People

class create_user_form(forms.Form):
    name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10,widget=forms.PasswordInput)

    class Meta:
        model = People

class Post_form(forms.Form):
    post_content = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'autocomplete':'off'}))
    class Meta:
        model = Posts

