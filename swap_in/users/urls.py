# Users URLS

# Django
from django.urls import path

# views
from users.views import (
    UserLoginAPIView,
    list_users,
    create_user,
) 

urlpatterns = [
    path('users/', list_users),
    path('users/create/', create_user),
    path('users/login/', UserLoginAPIView.as_view(), name='login')
]

