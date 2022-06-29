from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from post.serializers import PostSerializer
from .models import Post as PostModel


# Create your views here.
class PostView(APIView):
    # 포스트 조회
    
    # 포스트 업로드
    def post(self, request):
        request.data['artist'] = request.user.id
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
    def delete(self, request):
        return Response({'message': '삭제 성공!'})