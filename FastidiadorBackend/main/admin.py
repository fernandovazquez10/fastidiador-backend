from django.contrib import admin

from .models import StatusDia, UserCurso


@admin.register(StatusDia)
class StatusDiaAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'dia',
        'status'
    )

    
@admin.register(UserCurso)
class UserCursoAdmin(admin.ModelAdmin):
    fields = (
        '__all__',
    )
