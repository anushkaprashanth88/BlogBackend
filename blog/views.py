from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from blog.serializer import BlogSerializer
from blog.models import UserModel
from blog.models import BlogModel
from blog.serializer import PostSerializer
from django.db.models import Q

# Create your views here.
@csrf_exempt
def addUser(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        print(json.dumps(recieved_data))
        serializer_check = BlogSerializer(data=recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse({json.dumps({"status":"success"})})
        else:
            return HttpResponse({json.dumps({"status":"failed"})})
        
@csrf_exempt
def viewUser(request):
    if request.method =="POST":
        userList = UserModel.objects.all()
        serialize_data = BlogSerializer(userList,many=True)
        return HttpResponse({json.dumps(serialize_data.data)})
    
@csrf_exempt
def addPost(request):
    if request.method =="POST":
        post_data = json.loads(request.body)
        print(json.dumps(post_data))
        serializer_check = PostSerializer(data=post_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse({json.dumps({"status":"success"})})
        else:
            return HttpResponse({json.dumps({"status":"failed"})})
        
@csrf_exempt
def viewAll(request):
    if request.method == "POST":
        viewList = BlogModel.objects.all()
        serialize_data = PostSerializer(viewList,many=True)
        return HttpResponse({json.dumps(serialize_data.data)})
    
@csrf_exempt
def viewPost(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        getuserid = recieved_data["userid"]
        data = list(BlogModel.objects.filter(Q(userid__icontains = getuserid)).values())
        return HttpResponse(json.dumps(data))

