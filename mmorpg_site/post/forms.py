from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from django_ckeditor_5.fields import CKEditor5Field

from .models import Post


class AdminPostCreationForm(forms.ModelForm):
    """Форма созданий объявлений через админ панель"""
    class Meta:
        model = Post
        fields = ['title', 'text', 'user', 'category']


class AdminPostChangeForm(forms.ModelForm):
    """Форма изменения объявлений через админ панель"""
    class Meta:
        model = Post
        fields = ['title', 'text']


class PostCreationForm(forms.ModelForm):
    """Форма созданий объявлений. Дополнительные настройки CKEditor5"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    text = forms.CharField(widget=CKEditor5Widget(config_name='extends'))

    class Meta:
        model = Post
        fields = ['title', 'text', 'category']
