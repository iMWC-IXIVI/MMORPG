from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives

from .models import Response


@receiver(post_save, sender=Response)
def response_created(sender, instance, created, **kwargs):
    """Во время создании отклика приходит письмо на почту создателю поста.
    Во время активации отклика приходит письмо на почту создателя отклика"""
    if created:
        subject = 'You have response'
        email = instance.post.user.email
        html_content = (f'<h1>You have a response at post</h1>'
                        f'<p>Id post: {instance.post.pk}</p>'
                        f'<p>Title post: {instance.post.title}</p>'
                        f'<p>User response: {instance.user}</p>')
    else:
        subject = 'Your response is activate'
        email = instance.user.email
        html_content = (f'<h1 align="center">Hello {instance.user}, your response an activated</h1>'
                        f'<h2>YOUR TEXT RESPONSE: {instance.text}</h2>'
                        f'<h2>CATEGORY: {instance.post.category}</h2>'
                        f'<h2>AUTHOR POST: {instance.post.user}')

    message = EmailMultiAlternatives(subject=subject,
                                     to=[email])
    message.attach_alternative(html_content, mimetype='text/html')
    message.send()
