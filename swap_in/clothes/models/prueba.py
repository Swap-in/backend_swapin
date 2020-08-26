from django.db import models

class Prueba(models.Model):
    description = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pictures/')