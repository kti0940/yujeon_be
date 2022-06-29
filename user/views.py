from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from user.serializers import UserSignUpSerializer

import os


# Create your views here.

class UserView(APIView):
    def get(self, request):
        user = request.user
        print(user)
        return Response({"message":"get !!"})
    
    # 회원가입 
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"회원가입에 성공했습니다!"})
        else:
            print(serializer.errors)
            return Response({"message": "회원가입 실패"})

    def put(self, request):
        pass

    def delete(self, request):
        pass

class UserAPIView(APIView):
    
    # 로그인
    def post(self, request):
        username = request.data.get("username",'')
        password = request.data.get("password",'')

        user = authenticate(request, username=username, password=password)
        print(user)
        
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다"})
        
        
        login(request, user)  
        
        return Response({"message": "login success!!"})
    # 로그아웃
    def delete(self, request):
        logout(request)
        return Response({"로그아웃 성공 안녕히가세요"})

class ModelView(APIView):
    def post(self, request):
        print("머신러닝 모델 셋업")
        os.system("dir")
        # os.system("cd ./style-transfer-pytorch")
        os.chdir("style-transfer-pytorch")
        os.system("dir")
        os.system("style_transfer input_image.jpg input_style.jpg")
        os.system('taskkill /f /im python.exe')
        return Response("이미지 WIP")