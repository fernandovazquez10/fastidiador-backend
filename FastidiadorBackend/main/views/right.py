from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from main.models import Right


class ApiAuthRightsViewSet(ObtainAuthToken):
    @staticmethod
    def get(request, *arg, **kwargs):
        user = request.user
        group_right_ids = user.groups.exclude(groupright__isnull=True).values_list('groupright__id', flat=True)
        rights = Right.objects.filter(rigths__in=group_right_ids).values_list('name', flat=True)
        data = {
            "user_id": user.pk,
            "rights": set(rights),
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }
        return Response(data)
