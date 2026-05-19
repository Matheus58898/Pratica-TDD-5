from django import forms
from core.models import LinkModel

class LinkModelForm(forms.ModelForm):
    class Meta:
        model = LinkModel
        fields = ['titulo', 'link', 'observacao']