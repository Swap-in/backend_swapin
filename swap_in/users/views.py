""" Users views """

# Django
from django.shortcuts import redirect

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

# Models
from swap_in.clothes.models import Clothes

# Serializers
from swap_in.users.serializers import (
    CreateUserSerializer,
    UserLoginSerializer,
    UserModelSerializer,
    VerificationAccountSerializer
)
from swap_in.clothes.serializers import ClothesByUsersSerializer

# Utilities
import random

class UserLoginAPIView(APIView):
    """User Login API View"""
    permission_classes = (AllowAny,)
    
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
    permission_classes = (AllowAny,)
    
    def post(self, request, *args, **kwargs):
        """Handle HTTP Post request"""
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)


class VerificationAccountAPIView(APIView):
    """ Verification Account View """
    permission_classes = (AllowAny,)
    authentication_classes = []

    def get(self, request):
        """ Verify account """
        verify_token = request.GET['token']
        print(verify_token)
        token_dict = {'token': verify_token}
        serializer = VerificationAccountSerializer(data=token_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return redirect('https://swapin.vercel.app/login')

@api_view(['GET'])
def Home(self):
    clothes = Clothes.objects.all()
    data=[]
    for clothe in clothes:
        home = {
            'id': clothe.id,
            'title': clothe.title,
            'description': clothe.description,
            'pictures': {
                clothe.picture_1,
                clothe.picture_2,
                clothe.picture_3,
                clothe.picture_4,
                clothe.picture_5
            },
            'category_id': clothe.category_id.description,
            'gender': clothe.gender,
            'brand': clothe.brand,
            'user_id': clothe.user_id.id,
            'username': clothe.user_id.username,
            'profile_picture': clothe.user_id.picture
        }
        data.append(home)
    random.shuffle(data)
    return Response(data)
    

class ListClothesByUserAPIView(APIView):
    """ List clothes by User """
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        """ Get all clothes for the user """
        obj = self.get_objects(id)
        serializer = ClothesByUsersSerializer(obj).data
        return Response(serializer)

    def get_objects(self, id):
        user_clothes = Clothes.objects.filter(user_id=id)
        obj = {'clothes_by_user': user_clothes}
        return obj
