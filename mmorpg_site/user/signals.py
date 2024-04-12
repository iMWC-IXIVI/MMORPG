import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate

from .models import EmailAccept

from dotenv import load_dotenv


load_dotenv()  # Загрузка переменных окружения


@receiver(post_save, sender=EmailAccept)
def accept_mail(sender, instance, created, **kwargs):
    """Отправка писем пользователями, которые:
    1. Регистрируются на форуме.
    2. Авторизуются на форуме"""

    if instance.username:
        subject = 'Activate register'
        html_content = (f'<h1>Hello {instance.username}</h1>'
                        f'<p>You have registered on the forum.'
                        f'Please <a href="{os.getenv("REF_TOKEN")}{instance.token}">activate</a> your profile</p>')
    else:
        subject = 'Activate sign in'
        user = authenticate(email=instance.email, password=instance.password)
        html_content = (f'<h1>Hello {user}</h1>'
                        f'<p>You are visiting our forum.'
                        f'Please <a href="{os.getenv("REF_TOKEN_IN")}{instance.token}">activate</a> your profile</p>')

    message = EmailMultiAlternatives(subject=subject,
                                     to=[instance.email])
    message.attach_alternative(html_content, mimetype='text/html')
    message.send()
