from django.db import models

from .likes import like
from swap_in.utils.models import SwapinModel


class notification(SwapinModel):
    date = models.DateTimeField(null=False)
    read = models.BooleanField(default=False)
    send = models.BooleanField(default=False)
    like_id = models.ForeignKey(like,on_delete=models.CASCADE)