from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
            post_serializer.save()
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
