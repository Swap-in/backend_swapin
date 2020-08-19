""" Users Serializers """

# Django
from django.contrib.auth import authenticate

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

# Models
from users.models import User

class UserModelSerializer(serializers.ModelSerializer):
    """ User model serializer. """
    class Meta:
        """Meta class """
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )


class UserSerializer(serializers.Serializer):
    """ Users Serializers. """
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    picture = serializers.CharField()
    gender = serializers.CharField()
   # token = serializers.IntegerField() // lo mostramos o no?

class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=60)
    password = serializers.CharField()
    first_name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=40)
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    phone_number = serializers.CharField(
        min_length=13,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    gender = serializers.CharField(max_length=6)

    def create(self, data):
        """ Create user """
        return User.objects.create(**data)

class UserLoginSerializer(serializers.Serializer):
    """ User Login serializers """

    username = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def validate(self, data):
        """ Verifiy credentials. """
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data
    
    def create(self, data):
        """ Generate or retrieve new token """
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key