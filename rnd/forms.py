from django import forms
from .models import Case
import datetime

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['creation_date', 'organization', 'summary', 'file', 'writer']

    creation_date = forms.DateField(
        label="작성일자",
        initial=datetime.date.today().strftime('%Y-%m-%d'),
        widget=forms.DateInput(attrs={'class': 'form-control', 'readonly': 'True'})
    )
    
    organization = forms.ChoiceField(
        choices=Case.ORG,
        label="기관 구분",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    summary = forms.CharField(
        label="피드백 요약",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '내용'})
    )

    file = forms.FileField(
        label="검토 보고서",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    writer = forms.CharField(
        label="작성자",
        widget=forms.TextInput(attrs={'class': 'form-control',  'placeholder': '담당자명'})
    )
