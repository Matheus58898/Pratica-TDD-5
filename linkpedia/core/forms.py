from django import forms
from core.models import LinkModel

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail institucional'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )

class LinkModelForm(forms.ModelForm):
    class Meta:
        model = LinkModel
        fields = ['titulo', 'link', 'observacao']