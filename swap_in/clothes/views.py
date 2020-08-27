from django.shortcuts import render
import datetime

# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.renderers import JSONRenderer

#models
from swap_in.clothes.models import like
from swap_in.clothes.models import Clothes
from swap_in.clothes.models import notification
from swap_in.users.models import User
from swap_in.clothes.models import Match
from swap_in.clothes.models import Prueba


def count_likes(clothes_id):
    """Count number of like for type"""
    
    likes = like.objects.filter(clothes_id =clothes_id, type_like = 'LIKE').count()
    superlikes = like.objects.filter(clothes_id =clothes_id, type_like = 'SUPERLIKE').count()
    dislikes = like.objects.filter(clothes_id =clothes_id, type_like = 'DISLIKE').count()

    data=[{
        "clothes_id":clothes_id,
        "LIKE":likes,
        "SUPERLIKE":superlikes,
        "DISLIKE":dislikes
    }]

    return data

@api_view(['POST'])
def create_like(request):

    new_like = like()
    new_like.clothe_id = Clothes.objects.get(id = request.data['clothe_id']) 
    new_like.user_id = User.objects.get(id = request.data['user_id']) 
    new_like.type_like = request.data['type_like']
    new_like.save()
    data=[]
    if request.data['type_like'] == 'LIKE' or request.data['type_like'] == 'SUPERLIKE':
        create_notification(new_like)
        if request.data['type_like'] == 'SUPERLIKE':
            item = search_match(new_like)
        else:
            item = {
                "match":False
            }
    else:        
        item = {
            "match":False
        }
        
    data.append(item)



    # num_likes_clothes = count_likes(request['clothe_id'])
    # return Response(num_likes_clothes,status=status.HTTP_200_OK)
    return Response(data,status=status.HTTP_200_OK)


def create_notification(like):
    new_notification = notification()
    new_notification.date = datetime.date.today()
    new_notification.like_id = like
    new_notification.read = False
    new_notification.send = False
    new_notification.status = 'ACTIVE'
    new_notification.save()
    

@api_view(['GET'])
def num_notification(user_id):
    num_not = notification.objects.filter(like_id__clothe_id__user_id = user_id).count()

    return Response(num_not,status=status.HTTP_200_OK)

@api_view(['GET'])
def list_notifications_by_user(self,id):
    clothes_filter = Clothes.objects.filter(user_id__id=id)
    # user_notif = User.objects.filter(id=id)
    notification_filter = notification.objects.filter(like_id__clothe_id__in = [clothes.id for clothes in clothes_filter],read = False).order_by('-date')
    # print(user_notif)
    data = []

    for item in notification_filter:
        item_data = {
            "user_id":item.like_id.user_id.id,
            "user_name":item.like_id.user_id.first_name + ' ' + item.like_id.user_id.last_name,
            "picture": item.like_id.user_id.picture,
            "type_like": item.like_id.type_like,
            "clothe_id": item.like_id.clothe_id.id,
            "notification_id": item.id
        }

        data.append(item_data)

    return Response(data,status=status.HTTP_200_OK)



@api_view(['POST'])
def notification_read(request):
    read_notification = notification.objects.get(id=request.data['notification_id'])
    read_notification.read=True
    read_notification.save()
    return Response(read_notification.id,status=status.HTTP_201_CREATED)


def search_match(like_user):
    user_id_like = like_user.user_id    # usuario que dio el like
    
    user_id_clothe = like_user.clothe_id.user_id # usuario al que se le dio like
    
    clothes_filter = Clothes.objects.filter(user_id__id=user_id_like.id) # prendas del usuario que le dio like

    likes = like.objects.filter(clothe_id__in = [clothes.id for clothes in clothes_filter],type_like='SUPERLIKE',user_id = user_id_clothe).count()
    

    if likes > 0:
        count_like = Match.objects.filter(user_like_id = user_id_like, user_clothe_id = user_id_clothe).count()
        count_clothe = Match.objects.filter(user_like_id = user_id_clothe, user_clothe_id = user_id_like).count()
        if count_like > 0 or count_clothe > 0:
            item = {
            "match" : False
            }
        else:
            new_Match = Match()
            new_Match.user_like = user_id_like
            new_Match.user_clothe = user_id_clothe
            new_Match.save()
            
            item = {
                "match" : True,
                "user_id": user_id_clothe.id,
                "picture": user_id_clothe.picture,
                "phone_number": user_id_clothe.phone_number,
                "type_like": like_user.type_like,
                "clothe_id": like_user.clothe_id.id

            }
    else:
        item = {
            "match" : False
        }

    return (item)




@api_view(['GET'])
def list_notifications_by_clothe(self,id):

    clothes_filter = Clothes.objects.get(id=id)
    # like_filter = like.objects.filter(clothe_id = clothes_filter).order_by()
    like_filter = notification.objects.filter(like_id__clothe_id = clothes_filter).order_by('-date')
    data =[]
    for item in like_filter:
        # print(item.like_id.clothe_id.id)
        # notif = notification.objects.filter(like_id=item)
        item_data = {
            "user_id":item.like_id.user_id.id,
            "user_name":item.like_id.user_id.first_name + ' ' + item.like_id.user_id.last_name,
            "picture": item.like_id.user_id.picture,
            "type_like": item.like_id.type_like,
            "clothe_id": item.like_id.clothe_id.id,
            "notification_id": item.id
        }

        data.append(item_data)

    return Response(data,status=status.HTTP_200_OK)


@api_view(['POST'])
def save_image(requests):
    with open(requests.data['ruta'],mode="r") as photo:
        prueba1 = Prueba()
        prueba1.description="Esto es una prueba1"
        prueba1.picture = photo
        prueba1.save()

    return Response("OK",status=status.HTTP_200_OK)
    
        


