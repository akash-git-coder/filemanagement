from django import forms
from django.contrib.auth.models import User

from .models import Files


class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('comment', 'file')

    def clean(self):
        cleaned_data = super(FileForm, self).clean()
        file = cleaned_data['file']

        if file:
            filename = file.name
            if not (filename.endswith('.html') or filename.endswith('.docx') or filename.endswith(
                    '.pdf') or filename.endswith('.txt')):
                raise forms.ValidationError('File format not supported!')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
