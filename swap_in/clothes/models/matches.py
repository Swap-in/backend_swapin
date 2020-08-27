from django.db import models
from swap_in.users.models import User

class Match(models.Model):
    user_like = models.ForeignKey(User,on_delete=models.CASCADE,null=False,related_name="user_likes")
    user_clothe = models.ForeignKey(User,on_delete=models.CASCADE,null=False,related_name="user_clothes")