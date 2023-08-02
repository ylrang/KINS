from django import forms
from .models import Data, Document

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['document', 'file']

    document = forms.ModelChoiceField(
        queryset=Document.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
