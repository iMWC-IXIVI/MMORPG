from django import forms

from .models import Response


class AdminResponseCreationForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'


class AdminResponseChangedForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'


class ResponseCreateForm(forms.ModelForm):

    text = forms.CharField(widget=forms.Textarea(attrs={"size": '50'}),
                           max_length=100,
                           label='Enter your text')

    class Meta:
        model = Response
        fields = ['text']
