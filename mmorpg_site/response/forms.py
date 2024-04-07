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
