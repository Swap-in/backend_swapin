from rest_framework import serializers

from swap_in.clothes.models.categories import category
from swap_in.clothes.models.clothes import Clothes

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
    id = serializers.IntegerField()
    description = serializers.CharField()


