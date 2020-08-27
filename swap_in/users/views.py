""" Users views """

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Models
from swap_in.users.models import User

# Serializers
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
        verify_token = request.GET['token']
        token_dict = {'token': verify_token}
        print(verify_token)
        serializer = VerificationAccountSerializer(data=token_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message':'Cool, make some swaps'}
        return Response(data, status=status.HTTP_200_OK)
    

class UsersListAPIView(generics.ListCreateAPIView):
    """ List users. """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated]
    authentication_class = [TokenAuthentication]