from django.urls import path

from swap_in.users.views import (
    UserSignUpAPIView,
    UserLoginAPIView,
    Home,
    VerificationAccountAPIView,
) 

urlpatterns = [
    path('home/', Home.as_view(), name='users'),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/verify/', VerificationAccountAPIView.as_view(), name='verify'),
]

 