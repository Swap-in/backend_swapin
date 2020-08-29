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

class ClothesByUsersSerializer(serializers.Serializer):
    """ List clothes by user """

    clothes_by_user = UserClothesSerializer(many=True)
    
    class Meta:
        """ Meta class """
        fields = ('clothes_by_user')
    