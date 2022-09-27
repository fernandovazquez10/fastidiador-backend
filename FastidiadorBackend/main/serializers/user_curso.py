from rest_framework import serializers

from main.models import UserCurso


class UserCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCurso
        fields = (
            '__all__',
        )
