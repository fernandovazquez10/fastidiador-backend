from tabnanny import verbose
from django.db import models


class UserCurso(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    curso = models.CharField(max_length=300, blank=True, null=True)
    activo = models.BooleanField(default=True)
    url_curso = models.URLField(blank=True, null=True, verbose_name="URL del curso")
    fecha_inicio = models.DateField(blank=True, null=True, verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(blank=True, null=True, verbose_name="Fecha de finalización")
    ulr_certificado = models.URLField(blank=True, null=True, verbose_name="URL del certificado")

    def __str__(self):
        return f"{self.user} - {self.curso}"

    class Meta:
        verbose_name = "User - Curso"
        verbose_name_plural = "User - Cursos"