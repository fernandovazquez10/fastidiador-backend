from tokenize import group
from django.contrib.auth.models import Group
from django.db import models


class GroupRight(models.Model):
    rights = models.ManyToManyField('main.Right', related_name="rigths")
    group = models.OneToOneField(Group, on_delete=models.OneToOneField)

    def __str__(self):
        return self.group.name
    
    class Meta:
        verbose_name = "Rigths - Group"
        verbose_name_plural = "Rigths - Groups"
        