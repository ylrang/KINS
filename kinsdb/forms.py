from django import forms
from .models import Document
from django.db.models import CharField


class DataForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'institution', 'serial_num', 'file', 'csv']

    title = forms.CharField(
        label="문서명",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    institution = forms.CharField(
        label="국가/기관",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    serial_num = forms.ModelChoiceField(
        label="문서 분류",
        queryset=Document.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    file = forms.FileField(
        label="번역본",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    csv = forms.FileField(
        label="csv 데이터",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
