from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from blog.serializer import BlogSerializer

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