from django.db import models

from django_ckeditor_5 import fields

from user.models import CustomUser

from .constant import CHOICE


class Post(models.Model):
    """Модель объявления"""
    title = models.CharField(max_length=100, verbose_name='Title')
    text = fields.CKEditor5Field('Text', config_name='extends')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=25, choices=CHOICE)

    USERNAME_FIELD = 'user'

    def __str__(self):
        return f'{self.user}: {self.title}'
