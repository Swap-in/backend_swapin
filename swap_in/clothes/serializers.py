""" Clothes Serializers """

# Django REST Framework 
from rest_framework import serializers

# Models
from swap_in.clothes.models import Clothes, category

class ClothesSerializer(serializers.ModelSerializer):
    """ User clothes serializer """
    class Meta:
        model = Clothes
        fields = '__all__'

class ClothesByUsersSerializer(serializers.Serializer):
    """ List clothes by user """
    clothes_by_user = ClothesSerializer(many=True)
    
    class Meta:
        fields = ('clothes_by_user')

class CategorySerializer(serializers.Serializer):
    """ List clothes by category """
    clothes = ClothesSerializer(many=True)

    class Meta:
        fields = ('clothes')