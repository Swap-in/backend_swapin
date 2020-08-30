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
    get_categories,
    search_clothes_by_category,
    UsersClothesAPIView
)

router = DefaultRouter()
router.register(r'user/clothes', UsersClothesAPIView, 'clothes')
urlpatterns = router.urls

urlpatterns += [
    path('clothes/like/',create_like),
    path('clothes/notification_user/<int:id>/',list_notifications_by_user),
    path('clothes/notification_clothe/<int:id>/',list_notifications_by_clothe),
    path('clothes/notification_read/',notification_read),
    path('clothes/get_categories/<int:id>/',get_categories),
    path('clothes/search_clothes/<int:id_category>/<int:id_user>/',search_clothes_by_category)

]