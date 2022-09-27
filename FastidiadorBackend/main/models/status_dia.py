from email.policy import default
from tabnanny import verbose
from django.db import models


class StatusDia(models.Model):
    EN_PROGRESO = 1
    SIN_ESTUDIAR = 2
    ESTUDIADO = 3

    STATUS = (
        (EN_PROGRESO, "Dia en progreso"),
        (SIN_ESTUDIAR, "Dia sin estudiar"),
        (ESTUDIADO, "Dia estudiado")
    )
    
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    dia = models.DateField(blank=True, null=True)
    status = models.SmallIntegerField(choices=STATUS, default=EN_PROGRESO)

    def __str__(self):
        return f"{self.dia} - {self.user} - {self.get_status_display()}"

    class Meta:
        verbose_name = "Status - Dia"
        verbose_name_plural = "Status - Dias"
