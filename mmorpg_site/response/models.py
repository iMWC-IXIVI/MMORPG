from django.db import models

from post.models import Post
from user.models import CustomUser


class Response(models.Model):
    response = models.BooleanField(default=False, verbose_name='Response')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'user'

    def __str__(self):
        return f'{self.user}: {self.post.title}'
