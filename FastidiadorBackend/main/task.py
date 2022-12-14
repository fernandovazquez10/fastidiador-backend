from asyncio import tasks
import imp
from operator import sub
from celery import shared_task
from main.models import StatusDia
from datetime import datetime
from django.contrib.auth.models import User
from post_office import mail
from FastidiadorBackend.utils import template_correo
from FastidiadorBackend.settings import DEFAULT_FROM_EMAIL

@shared_task(bind=True,
            name="create_status-dia",
            max_retries=3
            )
def create_status_dia(self):
    for user in User.objects.all():
        StatusDia.objects.create(
            user=user,
            status=StatusDia.EN_PROGRESO,
            dia=datetime.now().date()
        )


@shared_task(bind=True, name="send_mail_progress")
def send_mail_progress(self):
    for dia_no_estudiado in StatusDia.objects.filter(status=1):
        dia_no_estudiado.status = 2
        dia_no_estudiado.save()
        mail.send(
            dia_no_estudiado.user.email,
            DEFAULT_FROM_EMAIL,
            subject=f"No pierdas tu progreso {dia_no_estudiado.user.first_name}",
            html_message=template_correo,
            message="Estudia hoy y no pierdas conocimiento valioso",
            priority='now'
        )
