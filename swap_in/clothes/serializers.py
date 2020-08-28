""" Clothes Serializers """

# Django REST Framework 
from rest_framework import serializers

# Models
from swap_in.clothes.models import Clothes

class UserClothesSerializer(serializers.ModelSerializer):
    """ User clothes serializer """

    class Meta:
        """ Meta class """
        model = Clothes
        fields = '__all__'