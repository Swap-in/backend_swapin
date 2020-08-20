#Django Models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from swap_in.utils.models import SwapinModel
from users.models.countries import country


TYPE_GENDER = [
        ("FEMALE","FEMALE"),
        ("MALE","MALE"),
        ("OTHER","OTHER")
        ]

class User(SwapinModel,AbstractUser):
    """Swap.in User
    
    Extend from Django's Abstract User
    """
    # email = models.EmailField(
    #     'email address',
    #     unique=True,
    #     error_messages ={
    #         'unique':'A user with that email already exists.'
    #     }
    # )

    phone_regex = RegexValidator(
        regex = r'\+?1?\d{9,15}$',
        message = "Phone number must be entered in th format: +999999999999. Up to 15 digits allowed."
    )

    phone_number = models.CharField(validators=[phone_regex],
        max_length=17,blank=True
    )

    
    picture = models.CharField(max_length=500,blank=True,null=True)

    gender = models.CharField(max_length=8,choices=TYPE_GENDER)

    token = models.IntegerField(null=True)

    is_verified = models.BooleanField(default=False)

    country_id = models.ForeignKey(country,on_delete=models.CASCADE, null=False)

    # REQUIRED_FIELDS = ['username','first_name','last_name','phone_number']