# Users URLS

# Django
from django.urls import path

# views
from swap_in.users.views import (
    UserSignUpAPIView,
    UserLoginAPIView,
    UsersListAPIView,
    VerificationAccountAPIView,
    Logout,
) 

urlpatterns = [
    path('users/', UsersListAPIView.as_view(), name='users'),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/verify/', VerificationAccountAPIView.as_view(), name='verify'),
    path('users/logout/', Logout.as_view(), name='logout'),
]

 