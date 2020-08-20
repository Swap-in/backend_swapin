""" Users Serializers """

# Django
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

# Models
from users.models import User

class UserModelSerializer(serializers.ModelSerializer):
    """ User model serializer. """
    class Meta:
        """ Meta class """
        model = User
        fields = '__all__'
        # fields = (
        #     'username',
        #     'first_name',
        #     'last_name',
        #     'email',
        #     'phone_number'
        # )

class UserSerializer(UserModelSerializer):
    """ Users Serializers. """
    # username = serializers.CharField()
    # password = serializers.CharField()
    # # first_name = serializers.CharField()
    # # last_name = serializers.CharField()
    # email = serializers.EmailField()
    # phone_number = serializers.CharField()
    # picture = serializers.CharField()
    # gender = serializers.CharField()
   # token = serializers.IntegerField() // lo mostramos o no?

class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    password = serializers.CharField(min_length=8)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    phone_regex = RegexValidator(
        regex = r'\+?1?\d{9,15}$',
        message = "Phone number must be entered in th format: +999999999999. Up to 15 digits allowed."
    )
    phone_number = serializers.CharField(
        min_length=13,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
            phone_regex
        ]
    )
    gender = serializers.CharField(max_length=6)

    def create(self, data):
        """ Create user """
        user = User.objects.create(**data, is_verified=False)
        user.set_password(data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    """ User Login serializers """

    username = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def validate(self, data):
        """ Verify credentials. """
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_verified:
            raise serializers.ValidationError('Account is not active yet, please verified your email to continue.')
        self.context['user'] = user
        return data
    
    def create(self, data):
        """ Generate or retrieve new token """
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key