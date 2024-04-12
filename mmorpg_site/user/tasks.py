from django.core.mail import EmailMultiAlternatives

from celery import shared_task

from datetime import date, timedelta

from post.models import Post
from .models import Subscribe


@shared_task
def every_monday_newsletter():
    """Еженедельная рассылка на количество постов за неделю"""
    today = date.today()

    while today.weekday() != 0:
        today -= timedelta(1)

    weekly_posts = Post.objects.filter(data_creation__date__gte=today)

    html_content = (f'<h1>Newsletter</h1>'
                    f'<h2>Count posts in weekly: {weekly_posts.count()}</h2>')

    for user in Subscribe.objects.all():
        message = EmailMultiAlternatives(subject='NEWSLETTER',
                                         to=[user.email])
        message.attach_alternative(html_content, mimetype='text/html')
        message.send()
