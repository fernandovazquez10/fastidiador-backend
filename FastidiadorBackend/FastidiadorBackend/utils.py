from ast import Mod
from re import M
from django.urls import URLPattern
from django.urls.resolvers import RegexPattern
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json

def process_querysrting(querysetring):
    filters = {}
    if querysetring:
        for filter_str in querysetring.split(";"):
            values = filter_str.split("==", 2)
            if len(values) == 2 and values[1] != "":
                filter[values[0]] == values[1]

class CustomRouter(DefaultRouter):
    def get_urls(self):
        urls = super(CustomRouter, self).get_urls()
        for prefix, viewset, basename in self.registry:
            if getattr(viewset, "model", None):
                fields = viewset.model._meta.fields
                for field in fields:
                    if field.choices:
                        name = "{}_choice_field_{}".format(viewset.model._meta.model_name, field.attname)
                        pattern = URLPattern(
                            RegexPattern(
                                '^{}/choice_field/{}/$'.format(prefix, field.attname),
                                name="choice_field", is_endpoint=True
                            ),
                            viewset.as_view({"get":name}, **dict()),
                            name="{}-choice_field_{}".format(basename, field.attname)
                        )
                        urls.append(pattern)
        return urls


class CustomModelViewSet(ModelViewSet):
    model = None
    paginator = None
    choice_fields = list()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    pagination_class = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def init(self, __):
        data = self.model.get_field_data(self.serializer_class)
        return Response(data)
    
    @action(detail=False, methods=['GET'])
    def select_list(self, __):
        queryset = self.filter_queryset(self.get_queryset)
        data = []
        for q in queryset[:20]:
            data.append({
                "id": q.pk,
                "value": q.__str__()
            })
        return Response(data)

    def get_choice(self, choices=None):
        data = []
        if  choices:
            for identidier, value in choices:
                data.append({
                    "id": identidier,
                    "value": value
                })

    def dispatch(self, request, *args, **kwargs):
        # noinspection PyAttributeOutsideInit
        self.args = args
        # noinspection PyAttributeOutsideInit
        self.kwargs = kwargs
        request = self.initialize_request(request, *args, **kwargs)
        # noinspection PyAttributeOutsideInit
        self.request = request
        # noinspection PyAttributeOutsideInit
        self.headers = self.default_response_headers

        try:
            self.initial(request, *args, **kwargs)

            # Get the appropriate handler method
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(),
                                  self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed

            response = handler(request, *args, **kwargs)
        except Exception as exc:
            handle_exception = True
            if "_choice_field_" in self.action:
                # noinspection PyBroadException
                try:
                    field_dict = next(item for item in self.choice_fields if item["name"] == self.action)
                    response = self.get_choice(field_dict['field'].choices)
                    handle_exception = False
                except Exception:
                    response = self.handle_exception(exc)
            if handle_exception:
                response = self.handle_exception(exc)
        # noinspection PyAttributeOutsideInit,PyUnboundLocalVariable
        self.response = self.finalize_response(request, response, *args, **kwargs)
        return self.response

    def __init__(self, *args, **kwargs):
        # noinspection PyProtectedMember
        fields = self.model._meta.fields
        choice_fields = list()
        for field in fields:
            if hasattr(field, "choices") and field.choices:
                # noinspection PyProtectedMember
                name = "{}_choice_field_{}".format(self.model._meta.model_name, field.attname)
                choice_fields.append(dict(name=name, field=field))
                setattr(self, name, self.get_choice())
        self.choice_fields = choice_fields
        super(CustomModelViewSet, self).__init__(*args, **kwargs)
            
template_correo = "Hola mundo"