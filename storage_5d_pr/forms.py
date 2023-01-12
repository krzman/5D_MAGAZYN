from django import forms


class FormLogin(forms.Form):
    username = forms.EmailField(max_length=64, label='Podaj maila')
    password = forms.CharField(max_length=64, label='Podaj hasło', widget=forms.PasswordInput)