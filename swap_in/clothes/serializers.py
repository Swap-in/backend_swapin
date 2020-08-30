""" Clothes Serializers """

# Django REST Framework 
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from swap_in.clothes.models import Clothes, category, like
from swap_in.users.models import User

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

class CategoryModelserializer(serializers.ModelSerializer):
    """ Category model serializer. """
    class Meta:
        """ Meta class """
        model = category
        fields = (
            'id',
            'description',            
        )

class CategorySerializer(serializers.Serializer):
    """Category serializer"""
    id = serializers.IntegerField()
    description = serializers.CharField()



