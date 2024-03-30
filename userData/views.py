from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import request
from userData.models import User
from userData.serializer import UserSerializer

# Create your views here.

class AddUser(APIView):
    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class GetUsers(APIView):
    def get(self,request,*args,**kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class getUserById(APIView):
    def get(self,request,userId,*args,**kwargs):
        try:
            user = User.objects.get(userId=userId)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error" : "User Not Found"}, status= status.HTTP_400_BAD_REQUEST)
        
class sortByName(APIView):
    def get(self,request,*args,**kwargs):
        users = User.objects.all().order_by("age")
        serializer = UserSerializer(users, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
