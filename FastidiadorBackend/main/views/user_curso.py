from FastidiadorBackend.utils import CustomModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from main.models import UserCurso
from main.serializers import UserCursoSerializer


class UserCursoViewSet(CustomModelViewSet):
    queryset = UserCurso.objects.all()
    serializer_class = UserCursoSerializer
    model = UserCurso
    
    def get_queryset(self):
        queryset = UserCurso.objects.filter(user=self.request.user)
        return queryset
    
    @action(detail=False, methods=['get'])
    def activos_list(self, request):
        cursos_activos_usuario = self.get_queryset().exclude(activo=False)
        data = []
        for curso in cursos_activos_usuario:
            data.append({
                "id": curso.pk,
                "name": curso.curso,
                "activo": curso.activo,
                "fecha_inicio": curso.fecha_inicio
            })
        return Response(data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def terminados_list(self, request):
        cursos_terminados_usuario = self.get_queryset().exclude(activo=True)
        data = []
        for curso in cursos_terminados_usuario:
            data.append({
                "id": curso.pk,
                "name": curso.curso,
                "activo": curso.activo,
                "fecha_inicio": curso.fecha_inicio
            })
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        curso : UserCurso = self.get_object()
        data = {
            "id": curso.pk,
            "activo": curso.activo,
            "url_curso": curso.url_curso,
            "fecha_incio": curso.fecha_fin,
            "fecha_fin": curso.fecha_fin or "-",
            "url_certificado": curso.url_certificado or "-",
        }
        return Response(data, status=status.HTTP_200_OK)