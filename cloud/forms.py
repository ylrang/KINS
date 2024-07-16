from django import forms
from .models import Post, Folder, Log, Files
from account.models import myUser
from django.db.models import CharField

class FileEditForm(forms.ModelForm):

    class Meta:
        model = Files
        fields = '__all__'

    files = forms.FileField(
        label="파일 업로드",
        required = False,
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'})
    )


class PostEditForm(forms.ModelForm):
    # SECTOR = (
    #     ('1', '기관 제출 공문'),
    #     ('2', '참여기관 공유'),
    #     ('3', '회의일정 및 전체자료'),
    #     ('4', '기타'),
    # )

    class Meta:
        model = Post
        fields = '__all__'

    title = forms.CharField(
        label="제목",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    description = forms.CharField(
        label="설명",
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    # sector = forms.ChoiceField(
    #     label="문서 분류",
    #     required=True,
    #     choices=SECTOR,
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )

    writer = forms.ModelChoiceField(
        label="작성자",
        required=True,
        queryset=myUser.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    tel = forms.CharField(
        label="연락처",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    folder = forms.ModelChoiceField(
        label="폴더",
        required=True,
        queryset=Folder.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class FileForm(forms.ModelForm):

    class Meta:
        model = Files
        exclude = ('log',)

    files = forms.FileField(
        label="파일 업로드",
        required = False,
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'})
    )


class PostForm(forms.ModelForm):
    SECTOR = (
        ('1', '기관 제출 공문'),
        ('2', '참여기관 공유'),
        ('3', '회의일정 및 전체자료'),
        ('4', '기타'),
    )

    class Meta:
        model = Post
        fields = '__all__'

    title = forms.CharField(
        label="제목",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    description = forms.CharField(
        label="설명",
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    # sector = forms.ChoiceField(
    #     label="문서 분류",
    #     required=True,
    #     choices=SECTOR,
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )

    writer = forms.ModelChoiceField(
        label="작성자",
        required=True,
        queryset=myUser.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    tel = forms.CharField(
        label="연락처",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    folder = forms.ModelChoiceField(
        label="폴더",
        required=True,
        queryset=Folder.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
