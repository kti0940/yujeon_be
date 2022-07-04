from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import os

# from post.serializers import PostGetSerializer, PostPostSerialize
from post.serializers import PostSerializer
from .models import Post as PostModel


# Create your views here.
class PostView(APIView):
    def get(self, request):
        posts = PostModel.objects.all()
        return Response(PostSerializer(posts, many=True).data)

 
    # 포스트 업로드
    def post(self, request):
        request.data['artist'] = request.user.id
        print(f'리퀘스트 데이터 -> {request.data}')
        post_serializer = PostSerializer(data=request.data)

        if post_serializer.is_valid():
            request.data['image']._set_name("input.jpg")
            post_serializer.save()
            run_model = ModelView()
            run_model.post(request)
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # 포스트 수정
    def put(self, request, post_id):
        post = PostModel.objects.get(id=post_id)
        post_serializer = PostSerializer(post, data=request.data, partial=True)
        
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # 포스트 삭제
    def delete(self, request):
        return Response({'message': '삭제 성공!'})
    
class ModelView(APIView):
    def post(self, request):
        print("머신러닝 모델 셋업")
        # os.system("dir") # 현재 위치에 존재하는 파일 확인
        os.chdir("deep_learning_with_images") # 터미널 cd 커맨드와 동일함 -> 폴더 이동
        # os.system("dir") # 폴더 이동했는지 한번 더 확인했음
        os.system('python main.py') # 머신러닝 모델 실행시키기
        os.chdir("..")
        os.remove('media/uploads/input.jpg')
        return Response("이미지 WIP")
    def delete(self, request, post_id):
        post = PostModel.objects.get(id=post_id)
        post.delete()
        return Response({'message': '삭제 성공!'})

class PostLikeView(APIView):
    def post(self, request, post_id):
        user = request.user
        post = PostModel.objects.get(id=post_id)
        likes = post.like.all()
        like_lists = []
        for like in likes:
            like_lists.append(like.id)
        if user.id in like_lists:
            post.like.remove(user)
            return Response({'message': '좋아요 취소!'})
        else:
            post.like.add(user)
            return Response({'message': '좋아요!'})


class PostDetailView(APIView):
    def post(self, request):
        postid = request.data['id']
        post = PostModel.objects.get(id=postid)
        serializer = PostSerializer(post).data 
        return Response(serializer)
