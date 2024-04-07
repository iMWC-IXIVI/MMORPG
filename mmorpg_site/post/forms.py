from django import forms

from .models import Post


class AdminPostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'user', 'category']


class AdminPostChangeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
