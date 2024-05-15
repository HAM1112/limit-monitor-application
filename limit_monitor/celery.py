from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import timedelta , crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'limit_monitor.settings')

app = Celery('limit_monitor')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'update-status-every-day': {
        'task': 'monitor.tasks.daily_status_update',
        'schedule': crontab(minute=0, hour=0),  # Runs daily at midnight
    },
    'update-status-every-month': {
        'task': 'monitor.tasks.monthly_status_update',
        'schedule': crontab(day_of_month=1, hour=0, minute=0),  # Runs on the 1st day of every month at midnight
    },
    'update-status-every-year': {
        'task': 'monitor.tasks.yearly_status_update',
        'schedule': crontab(day=1, month=1, hour=0, minute=0),  # Runs on the 1st day of every year at midnight
    },
    # 'update-status-every-day': {
    #     'task': 'monitor.tasks.update_status',
    #     'schedule': timedelta(seconds=15),  # Runs daily at midnight
    # },
}
