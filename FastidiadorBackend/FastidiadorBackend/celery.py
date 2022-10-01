from cgitb import enable
import os
from unittest import result
from celery import Celery
from celery.schedules import crontab
from pytz import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FastidiadorBackend.settings')

app = Celery('FastidiadorBackend')

app.config_from_object('djnago.conf:settings', namespace="CELERY",)

app.conf.update(
    result_expires=3600,
    enable_utc=True,
    timezone='America/Mexico_City'
)

app.conf.beat_schedule = {
    "every day at 12 AM": {
        "task": "create_dia-status",
        "schedule": crontab(
            hour='8',
            minute=10
        )
    },
    "every day an 8 PM": {
        "task": "send_mail_progress",
        "schedule": crontab(
            hour="20",
            minute=10
        )
    }
}

app.autodiscover_tasks()


