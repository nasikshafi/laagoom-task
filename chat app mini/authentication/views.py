from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from django.http import JsonResponse
from .models import Favorite

# Create your views here.

@csrf_exempt 
def signup(request):
    if request.method == "POST":
        received_json_data=json.loads(request.body)
        myuser= User.objects.create_user(received_json_data['username'],received_json_data['email'],received_json_data['password'])
        print ("woking",myuser)
    return HttpResponse("success")


@csrf_exempt 
def getuser(request):
    if request.method == "GET":
        users = User.objects.all().values()
        result =[]
        for values in users:
            result.append ({"id":values['id'],"username":values['username'],"email":values['email']}) 
        print("users",users,"'data",result)
    return JsonResponse(result,safe= False)



@csrf_exempt 
def signin(request):
    if request.method == "POST":
        received_json_data=json.loads(request.body)
        user = authenticate(username= received_json_data['username'],password= received_json_data['password'])
        print ("woking",user)
    return HttpResponse("success")



@csrf_exempt 
def addfavorite(request):
    if request.method == "POST":
        received_json_data=json.loads(request.body)
        user = User.objects.get(id=received_json_data['user_id'])
        print('user',user)
        favorites = Favorite(user_id = user)
        favorites.topics = received_json_data['topics']
        favorites.save()
        print ("woking",favorites)
    return HttpResponse("success")



@csrf_exempt 
def listfavorite(request):
    if request.method == "GET":
        favorites = Favorite.objects.all().values()
        print ("favorites",favorites)
        response =[]
        for values in favorites:
            response.append({
                "user_id": values['user_id_id'],
                'topics':values['topics']
            })
    return JsonResponse(response,safe= False)




@csrf_exempt 
def creategroup(request):
    if request.method == "POST":
        received_json_data=json.loads(request.body)
        group = Group.objects.create(name=received_json_data['group_name'])
        for values in received_json_data['users']:
            user= User.objects.get(id=values)
            group.user_set.add(user)
        print ('group',group)
    return HttpResponse("succcess")



@csrf_exempt 
def listgroups(request):
    if request.method == "GET":
        groups = Group.objects.all().values()
        print ("groups",groups)
        response =[]
        # for values in groups:
        #     response.append({
        #         "user_id": values['user_id_id'],
        #         'topics':values['topics']
        #     })
    return JsonResponse(response,safe= False)
