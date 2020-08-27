""" Users Serializers """

# Django
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template import Context
from django.template.loader import render_to_string
from django.utils import timezone
from django.conf import settings

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

# Models
from swap_in.users.models import User, Country

# Utilites
from datetime import timedelta
import jwt

class UserModelSerializer(serializers.ModelSerializer):
    """ User model serializer. """
    class Meta:
        """ Meta class """
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'picture'
        )

class UserSerializer(serializers.Serializer):
    """ Users Serializers. """
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    picture = serializers.CharField()
    gender = serializers.CharField()
    country_id = serializers.PrimaryKeyRelatedField(read_only=True)

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
    picture = serializers.CharField()
    gender = serializers.CharField(max_length=6)

    def create(self, data):
        """ Create user """
        user_country_id = Country.objects.get(id=1)
        user = User.objects.create(**data, is_verified=False, country_id=user_country_id)
        user.set_password(data['password'])
        user.save()
        self.send_confirmation_email(user)
        return user

    def send_confirmation_email(self, user):
        """ Send account verification link to the created user """
        verification_token = self.generate_token(user)
        subject = 'Confirm your account to make some swaps'
        from_email = settings.EMAIL_HOST_USER
        html_body = render_to_string(
            'verify_account.html',
            {
                'token': verification_token,
                'user': user
            }
        )
        mail = EmailMultiAlternatives(subject, html_body, from_email, [user.email])
        mail.attach_alternative(html_body, "text/html")
        mail.send()

    def generate_token(self,user):
        """ Generate verification token"""
        exp_date = timezone.now() + timedelta(days=1)
        payload = {
            "user": user.username,
            "exp": int(exp_date.timestamp()),
            "type": "email_confirmation"
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return token.decode()

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

class VerificationAccountSerializer(serializers.Serializer):
    """ Account Verification Serializer """

    token = serializers.CharField()

    def validate_token(self,data):
        """ Verify if token is valid or not """
        print(type(data))
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
            print(payload)
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token')
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Invalid token')
        self.context['payload'] = payload
        return data

    def save(self):
        """ Update is_verified status """
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()
            
