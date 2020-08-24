from django.db import models

from .clothes import clothes
from swap_in.users.models import User

TYPE_LIKE = [
    ("LIKE","LIKE"),
    ("SUPERLIKE","SUPERLIKE"),
    ("DISLIKE","DISLIKE")
]

class like(models.Model):
    type_like = models.CharField(max_length=15,choices=TYPE_LIKE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    clothe_id = models.ForeignKey(clothes,on_delete=models.CASCADE,null=False)


