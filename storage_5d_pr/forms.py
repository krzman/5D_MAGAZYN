from django import forms

from storage_5d_pr.models import *


class FormLogin(forms.Form):
    username = forms.EmailField(max_length=64, label='Podaj maila')
    password = forms.CharField(max_length=64, label='Podaj hasło', widget=forms.PasswordInput)


class FormToolsAdd(forms.ModelForm):
    class Meta:
        model = Tools
        fields = ['nr', 'type', 'producer', 'date', 'workers', 'construction']
        widgets = {
            'nr': forms.NumberInput(attrs={'step': '0.001'}),
            'date': forms.SelectDateWidget(),
        }
