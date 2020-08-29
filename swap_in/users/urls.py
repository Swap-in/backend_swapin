from django.urls import path

from swap_in.users.views import (
    UserSignUpAPIView,
    UserLoginAPIView,
    Home,
    VerificationAccountAPIView,
    ListClothesByUserAPIView
) 

urlpatterns = [
    path('home/', Home),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/verify/', VerificationAccountAPIView.as_view(), name='verify'),
    path('users/list_clothes/<int:id>/', ListClothesByUserAPIView.as_view(), name='users_clothes')
]

 