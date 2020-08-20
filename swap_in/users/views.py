"""Users views"""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Models
from users.models import User

# Serializer
from users.serializers import (
    UserSerializer,
    CreateUserSerializer,
    UserLoginSerializer,
    UserModelSerializer
)

class UserLoginAPIView(APIView):
    """User Login API View"""
    
    def post(self, request, *args, **kwargs):
        """Handle HTTP Post request"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)


# class UserSignUpAPIView(APIView):
#     """User Login API View"""
    
#     def post(self, request, *args, **kwargs):
#         """Handle HTTP Post request"""
#         serializer = UserSignUpSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         data = UserModelSerializer(user).data
#         return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_users(request):
    """ List users. """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    """ Create user. """
    serializer = CreateUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response(UserSerializer(user).data)