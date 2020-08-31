from django.urls import path, include

urlpatterns = [
    path('', include(('swap_in.users.urls', 'users'), namespace='user')),
    path('', include(('swap_in.clothes.urls', 'clothes'), namespace='clothes')),
]
