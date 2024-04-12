import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmorpg_site.settings')

app = Celery('mmorpg_site')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {'action_every_monday': {'task': 'user.tasks.every_monday_newsletter',
                                                  'schedule': crontab(day_of_week='monday')}}
