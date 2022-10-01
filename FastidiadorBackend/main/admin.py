from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import StatusDia, UserCurso


@admin.register(StatusDia)
class StatusDiaAdmin(admin.ModelAdmin):
    list_fields = (
        'user',
        'dia',
        'status'
    )

    
@admin.register(UserCurso)
class UserCursoAdmin(admin.ModelAdmin):
    fields = (
        '__all__',
    )
