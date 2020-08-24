from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('users.urls', 'users'), namespace='user')),
    path('admin/', admin.site.urls),
    path('',include(('clothes.urls','clothes'),namespace='clothes'))
]
