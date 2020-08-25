""" Users views """

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Models
from swap_in.users.models import User

# Serializer
from swap_in.users.serializers import (
    UserSerializer,
    CreateUserSerializer,
    UserLoginSerializer,
    UserModelSerializer,
    VerificationAccountSerializer
)

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
        """ Method provitional for accept token """
        return Response("")

    def post(self, request, *args, **kwargs):
        """ Verified the account to start swapin """
        serializer = VerificationAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message':'Cool, make some swaps'}
        return Response(data, status=status.HTTP_200_OK)
    

class UsersListAPIView(APIView):
    """ List users. """
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        """ List users. """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)