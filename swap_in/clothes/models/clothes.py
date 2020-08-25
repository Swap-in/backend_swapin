from django.db import models

# Create your models here.
from users.models import User
from swap_in.utils.models import SwapinModel
from clothes.models.categories import category

TYPE_GENDER = [
        ("FEMALE","FEMALE"),
        ("MALE","MALE"),
        ("OTHER","OTHER")
        ]

class Clothes(SwapinModel):
    title = models.CharField(max_length=150,null=False)
    description = models.CharField(max_length=500,null=False)
    category_id = models.ForeignKey(category,on_delete=models.CASCADE, null=False)
    size= models.CharField(max_length=20,null=False)
    gender = models.CharField(max_length=8,choices=TYPE_GENDER)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    picture_1  = models.CharField(max_length=500,blank=False,null=False)
    picture_2 = models.CharField(max_length=500,blank=True,null=True)
    picture_3 = models.CharField(max_length=500,blank=True,null=True)
    picture_4 = models.CharField(max_length=500,blank=True,null=True)
    picture_5 = models.CharField(max_length=500,blank=True,null=True)