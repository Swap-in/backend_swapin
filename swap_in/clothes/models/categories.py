# Django 
from django.db import models

class category(models.Model):
    """Category Model."""
    description = models.CharField(
        max_length=500,
        null=False
    )
