from rest_framework import serializers

from main.models import UserCurso


class UserCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCurso
        fields = (
            'id',
            'user',
            'curso',
            'activo',
            'url_curso',
            'fecha_inicio',
            'fecha_fin',
            'url_certificado'
        )
