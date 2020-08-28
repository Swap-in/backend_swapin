""" Users views """

# Django
from django.shortcuts import redirect

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Models
from swap_in.users.models import User
from swap_in.clothes.models import (
    like,
    Clothes,
    category
)

# Serializers
from swap_in.users.serializers import (
    UserSerializer,
    CreateUserSerializer,
    UserLoginSerializer,
    UserModelSerializer,
    VerificationAccountSerializer,
    LikesHomeSerializers,
    HomeSerializer
)

# Utilities
import random

class UserLoginAPIView(APIView):
    """User Login API View"""
    
    def post(self, request, *args, **kwargs):
        """Handle HTTP Post request"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        username = UserModelSerializer(user)
        data = {
            'message': f"Welcome {username.data['username']}",
            'token': token,
            'user': username.data
        }
        return Response(data, status=status.HTTP_200_OK)


class UserSignUpAPIView(APIView):
    """ User Login API View """
    
    def post(self, request, *args, **kwargs):
        """Handle HTTP Post request"""
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)


class VerificationAccountAPIView(APIView):
    """ Verification Account View """
    
    def get(self, request, *args, **kwargs):
        """ Verify account """
        verify_token = request.GET['token']
        token_dict = {'token': verify_token}
        serializer = VerificationAccountSerializer(data=token_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return redirect('localhost:8081/login')
    

class Home(APIView):
    """ List users. """
    permission_classes = [IsAuthenticated]
    authentication_class = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        """ Get all clothes for home app """
        home = Clothes.objects.all()
        # likes = like.objects.all()
        # serializer_like = LikesHomeSerializers(likes)
        serializer_home = HomeSerializer(home)
        return Response (serializer_home, status=status.HTTP_200_OK)