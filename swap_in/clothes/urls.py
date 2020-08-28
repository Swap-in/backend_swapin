# Django
from django.urls import path

# Django REST Framwork
from rest_framework.routers import DefaultRouter

# Views
from swap_in.clothes.views import (
    create_like,
    list_notifications_by_user,
    list_notifications_by_clothe,
    notification_read,
    save_image,
    UsersClothesAPIView
)

router = DefaultRouter()
router.register(r'user/clothes/', UsersClothesAPIView)
urlpatterns = router.urls

urlpatterns += [
    path('clothes/like/',create_like),
    path('clothes/notification_user/<int:id>/',list_notifications_by_user),
    path('clothes/notification_clothe/<int:id>/',list_notifications_by_clothe),
    path('clothes/notification_read/',notification_read),
    path('clothes/image/',save_image)
]