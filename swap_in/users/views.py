""" Users views """

# Django
from django.shortcuts import redirect

# Django REST Framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.authentication import TokenAuthentication

# Models
from swap_in.users.models import User
from swap_in.clothes.models import (
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
    HomeSerializer
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
    

# class Home(APIView):
#     """ Home application. """
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         """ Get all clothes for home app """
#         home = User.objects.all()
#         serializer_home = HomeSerializer(home, many=True).data
#         return Response (serializer_home, status=status.HTTP_200_OK)

@api_view(['GET'])
def Home(self):
    clothes = Clothes.objects.all()
    data=[]
    for clothe in clothes:
        home = {
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
    return Response(data)


# [
#      {  
#           prenda_1  : {
#               'user_id': user.id,
#               'username': user.username,
#               'profile_picture': user.picture,
#               'pictures': [
#                       'picture1',
#                       'picture2'
#                ]
#               'title': 'titulo de la prenda'
#               'description': 'descripcion de la prenda'
#             }
#      },
#      {  
#           prenda_2  : {
#               'user_id': user.id,
#               'username': user.username,
#               'profile_picture': user.picture,
#               'pictures': [
#                       'picture1',
#                       'picture2'
#                ]
#               'title': 'titulo de la prenda'
#               'description': 'descripcion de la prenda'
#             }
#      }
# ]

    

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