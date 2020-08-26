from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('swap_in.users.urls', 'users'), namespace='user')),
    path('admin/', admin.site.urls),
    path('',include(('swap_in.clothes.urls','clothes'), namespace='clothes')),
]
