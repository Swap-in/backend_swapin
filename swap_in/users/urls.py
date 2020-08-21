# Users URLS

# Django
from django.urls import path

# views
from users.views import (
    UserSignUpAPIView,
    UserLoginAPIView,
    list_users,
) 

urlpatterns = [
    path('users/', list_users),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('users/login/', UserLoginAPIView.as_view(), name='login')
]

