from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models


class Right(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Right"
        verbose_name_plural = "Rights"
