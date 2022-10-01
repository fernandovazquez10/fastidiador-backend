from rest_framework import serializers

from main.models import StatusDia


class StatusDiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusDia
        fields = (
            'id',
            'user',
            'dia',
            'status'
        )
