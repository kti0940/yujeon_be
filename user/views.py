from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth import login, logout, authenticate
from post import serializers
from user.serializers import UserSignUpSerializer, UserInfoSerializer

import os

from user.jwt_claim_serializer import YujeonTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication


# JWT 커스터마이저 시리얼라이저
class YujeonTokenObtainPairView(TokenObtainPairView):
    serializer_class = YujeonTokenObtainPairSerializer

class UserView(APIView):
    def get(self, request):
        user = request.user
        return Response(UserInfoSerializer(user).data)
    
    # 회원가입 
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"회원가입에 성공했습니다!"})
        else:
            return Response({"message": "회원가입 실패"})

    def put(self, request):
        return Response({"message":"put"})

    def delete(self, request):
        pass

class UserAPIView(APIView):
    
    # 로그인
    def post(self, request):
        username = request.data.get("username",'')
        password = request.data.get("password",'')

        user = authenticate(request, username=username, password=password)
        
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다"})
        
        
        login(request, user)  
        
        return Response({"message": "login success!!"})
    # 로그아웃
    def delete(self, request):
        logout(request)
        return Response({"로그아웃 성공 안녕히가세요"})



class UserLoginCehck(APIView):

    def get(self, request):
        return Response({"auth": "True"})