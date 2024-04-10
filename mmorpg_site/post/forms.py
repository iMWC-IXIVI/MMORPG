from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from django_ckeditor_5.fields import CKEditor5Field

from .models import Post


class AdminPostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'user', 'category']


class AdminPostChangeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class PostCreationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    text = forms.CharField(widget=CKEditor5Widget(config_name='extends'))

    class Meta:
        model = Post
        fields = ['title', 'text', 'category']
