from django import forms

from .models import Response


class AdminResponseCreationForm(forms.ModelForm):
    """Форма создания в админ панели"""
    class Meta:
        model = Response
        fields = '__all__'


class AdminResponseChangedForm(forms.ModelForm):
    """Форма редактирования в админ панели"""
    class Meta:
        model = Response
        fields = '__all__'


class ResponseCreateForm(forms.ModelForm):
    """Создание отклика"""
    text = forms.CharField(widget=forms.Textarea(attrs={"size": '50'}),
                           max_length=100,
                           label='Enter your text')

    class Meta:
        model = Response
        fields = ['text']
