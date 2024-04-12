from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import CustomUser


class AdminUserCreationForm(forms.ModelForm):
    """Форма для создания пользователя в админ панели"""
    email = forms.EmailField(max_length=255,
                             label='Email',
                             widget=forms.EmailInput,
                             help_text='Enter email for profile')

    password = forms.CharField(max_length=255,
                               label='Password',
                               widget=forms.PasswordInput,
                               help_text='Enter password for profile')

    username = forms.CharField(max_length=255,
                               label='Nickname',
                               widget=forms.TextInput,
                               help_text='Enter nickname at forum')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'image', 'is_staff', 'is_superuser']

    def save(self, commit=True):
        user_data = super().save(commit=False)
        user_data.set_password(self.cleaned_data['password'])

        if commit:
            user_data.save()

        return user_data


class AdminUserChangeForm(forms.ModelForm):
    """Изменение пользователя в админ панели"""
    password = ReadOnlyPasswordHashField()

    image = forms.ImageField(label='Change image',
                             widget=forms.FileInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'image', 'username', 'is_staff', 'is_superuser')


class UserUpdateForm(forms.ModelForm):
    """Изменение пользователя из страницы профиля пользователя"""

    image = forms.ImageField(widget=forms.FileInput, help_text='')

    class Meta:
        model = CustomUser
        fields = ['username', 'image']
