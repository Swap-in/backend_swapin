from django.db import models

class Country(models.Model):
    country_code = models.CharField(
        max_length=5,
        null=False
    )
    country_name = models.CharField(
        max_length=150,
        null=False
    )
