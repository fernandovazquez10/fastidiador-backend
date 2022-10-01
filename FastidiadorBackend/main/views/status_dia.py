from os import stat
from urllib import request
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from FastidiadorBackend.utils import CustomModelViewSet

from main.models import StatusDia
from main.serializers import StatusDiaSerializer

class StatusDiaViewSet(CustomModelViewSet):
    queryset = StatusDia.objects.all()
    serializer_class = StatusDiaSerializer
    model = StatusDia

    def get_queryset(self):
        queryset = StatusDia.objects.filter(user=self.request.user)
        return queryset
    
    @action(detail=False, methods=['get'])
    def custom_list(self, request):
        dias_list = self.get_queryset()
        data = []
        for dia_status in dias_list:
            data.append({
                'id': dia_status.pk,
                'status': dia_status.status,
                'dia': dia_status.dia
            })
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        status_dia : StatusDia = self.get_object()
        data = {
            "id": status_dia.pk,
            "status": status_dia.get_status_display(),
            "dia": status_dia.dia,
        }
        return Response(data, status=status.HTTP_200_OK)
