from importlib import import_module
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from main.models import Right


class ObtainAuthToken(ObtainAuthToken):
    def Post(self, request, *arg, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        group_right_ids = user.groups.exclude(groupright__isnull=True).values_list('groupright__id', flat=True)
        rights = Right.objects.filter(rights_id_in=group_right_ids).values_list('name', flat=True)
        data = {
            "token": token.key,
            "user_id": user.pk,
            "rights": set(rights)
        }
        return Response(data)