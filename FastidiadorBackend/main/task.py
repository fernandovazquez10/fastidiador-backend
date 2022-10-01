from asyncio import tasks
import imp
from operator import sub
from celery import shared_task
from main.models import StatusDia
from datetime import datetime
from django.contrib.auth.models import User
from post_office import mail

@shared_task(bind=True,
            name="create_status-dia",
            max_retries=3
            )
def create_status_dia(self):
    print("Almenos intente")
    for user in User.objects.all():
        StatusDia.objects.create(
            user=user,
            status=StatusDia.EN_PROGRESO,
            dia=datetime.now().date()
        )
        print("Almenos intente algo")


@shared_task(bind=True, name="send_mail_progress")
def send_mail_progress(self):
    for dia_no_estudiado in StatusDia.objects.filter(status=1):
        dia_no_estudiado.status = 2
        dia_no_estudiado.save()
        mail.send(
            dia_no_estudiado.user.email,
            "no_reply@ponchos.tech",
            subject="No pierdas tu progreso",
            html_message="Estudia hoy y no pierdas conocimiento valioso",
            message="Estudia hoy y no pierdas conocimiento valioso",
            priority='now'
        )
