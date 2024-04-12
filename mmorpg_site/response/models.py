from django.db import models

from post.models import Post
from user.models import CustomUser


class Response(models.Model):
    """Модель отклик"""
    text = models.CharField(max_length=100, verbose_name='Response')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    active = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='User')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Time created')

    USERNAME_FIELD = 'user'

    def __str__(self):
        return f'{self.user}: {self.post.title}'
