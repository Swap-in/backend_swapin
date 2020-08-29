from django.db import models

# Models
from swap_in.users.models import User
from swap_in.utils.models import SwapinModel
from .categories import category

TYPE_GENDER = [
        ("FEMALE","FEMALE"),
        ("MALE","MALE"),
        ("UNISEX","UNISEX")
        ]

class Clothes(SwapinModel):
    title = models.CharField(max_length=150,null=False)
    description = models.CharField(max_length=500,null=False)
    category_id = models.ForeignKey(category,related_name='category',on_delete=models.CASCADE, null=False)
    size = models.CharField(max_length=20,null=False)
    gender = models.CharField(max_length=8,choices=TYPE_GENDER)
    user_id = models.ForeignKey(User,related_name='clothes',on_delete=models.CASCADE)
    brand = models.CharField(max_length=100,blank=True,null=False)
    picture_1 = models.CharField(max_length=500,blank=False,null=False)
    picture_2 = models.CharField(max_length=500,blank=True,null=True)
    picture_3 = models.CharField(max_length=500,blank=True,null=True)
    picture_4 = models.CharField(max_length=500,blank=True,null=True)
    picture_5 = models.CharField(max_length=500,blank=True,null=True)