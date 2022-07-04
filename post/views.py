from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import datetime
import os
from post import serializers

# from post.serializers import PostGetSerializer, PostPostSerialize
from post.serializers import PostSerializer, CollectionSerializer
from .models import (
        Post as PostModel,
        Collection as CollectionModel
                     )
from user.models import (
        User as UserModel
)

import boto3


# Create your views here.

class PostView(APIView):
    def get(self, request):
        posts = PostModel.objects.filter(is_exposure=True).order_by('-created_at')
        return Response(PostSerializer(posts, many=True).data)

 
    # 포스트 업로드
    def post(self, request):
        print(f"request_data->{request.data}")
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
            
            post.cost -= 1
            print(f"post.cost 내림 ->{post.cost}")
            post.save()
            return Response({'message': '좋아요 취소!'})
        else:
            post.like.add(user)
            
            post.cost += 1
            post.save()
            print(f"post.cost 올림 ->{post.cost}")
            return Response({'message': '좋아요!'})


class PostDetailView(APIView):
    def post(self, request):
        postid = request.data['id']
        post = PostModel.objects.get(id=postid)
        serializer = PostSerializer(post).data 
        return Response(serializer)
    
class PurchaseArt(APIView):
    '''
    1. 구매할 그림의 값을 가져옴
    2. 구매하기를 누르면 나의 포인트 - 그림 포인트로 구매함
    5. 상대방 유저는 컬렉션에서 삭제
    3. 내 컬렉션 db에 내 유저 아이디로 레코드 추가
    4. 상대방 유저에게 내가 구매한 포인트만큼 포인트 추가됨
    '''
    def post(self, request, id):
        # 컬렉션의 가격 가져오기
        target_art = CollectionModel.objects.get(id=id)
        print(f"target_art->{target_art}")
        target_art_price = target_art.post.cost
        print(f"target_art_price->{target_art_price}")
        original_artist = UserModel.objects.get(id=target_art.owner.id)
        
        
        # 컬렉션 구매
        user = request.user
        print(f"user->{user}")
        owner_user = UserModel.objects.get(id=user.id)
        print(f"owner_user->{owner_user}")
        owner_user_point = owner_user.point
        print(f"owner_user_point->{owner_user_point}")
        
        print(f"유저는 누구입니까->{user}")
        
        # 1번 분기. 구매자와 소유자가 같을 경우 구매 불가
        if owner_user == target_art.owner:
            "구매불가"
            return Response("이미 소유한 미술품입니다")
        
        # 2번 분기. 포인트가 부족할 경우 구매 불가 
        if not owner_user_point >= target_art_price:
            "구매불가"
            return Response("포인트가 부족합니다")
        
        #구매가능한 상태
        print(f"오너 포인트 차감 전->{owner_user.point}")
        
        # 구매자의 포인트 차감
        owner_user.point = owner_user_point - target_art_price
        owner_user.save()
        print(f"오너 포인트 차감 후->{owner_user.point}")
        
        
        """
        구매자 데이터베이스 추가, 판매자 데이터베이스 삭제
        1. 구매자는 판매자와 동일한 PostModel의 레코드 생성
        2. 구매자의 PostModel 레코드의 is_mine 필드는 True
        3. 판매자의 PostModel 레코드의 is_mine 필드는 False
        4. 브라우저 리프레시
        ---
        구매했던 을의 그림을 병이 구매한 케이스
        1.  병은 을과 동일한 PostModel의 레코드 생성
        2. 구매자의 PostModel 레코드의 is_mine 필드는 True
        3. 판매자의 PostModel 레코드의 is_mine 필드는 False
        4. 브라우저 리프레시
        """
        
        # 판매자 접근 권한 지우기
        seller_post = PostModel.objects.get(id=target_art.post_id)
        
        seller_post.is_mine = False
        seller_post.save()

        # change_owner = PostModel.objects.get(id=target_art.owner.post_id)

        buyer_info = {
            "artist":owner_user,
            "title": seller_post.title,
            "image": seller_post.image,
            "artimage": seller_post.image,
            "desc" : seller_post.desc,
            "cost" : seller_post.cost,
            "is_mine" : True,
            "created_at" : seller_post.created_at,
            "is_exposure" : seller_post.is_exposure,
            "on_sale" : seller_post.on_sale,
        }
        buyer_post = PostModel.objects.create(**buyer_info)
        buyer_post.save()
        
        # 소유주 변경
        target_art.owner = owner_user
        target_art.post = buyer_post
        target_art.save()
        print(f"owner_user_point->{owner_user.point}")
        
        # 포인트 판매자에게 추가
        print(f"오리지널 아티스트->{original_artist.username}")
        print(f"아트 소유주->{target_art.owner.username}")
        reward_point = original_artist.point + target_art_price
        original_artist.point = reward_point
        original_artist.save()        
        #여기에서 변경된 소유주 오브젝트 불러서 is_mine False 처리 하면 되지않음?

        
        # 포인트 판매자에게 추가
        print(f"오리지널 아티스트->{original_artist.username}")
        print(f"아트 소유주->{target_art.owner.username}")
        reward_point = original_artist.point + target_art_price
        original_artist.point = reward_point
        original_artist.save()        
        return Response(f"{owner_user}의 남은 잔여 포인트는{owner_user.point}입니다")
        

class CollectionView(APIView):
    # 컬렉션 조회하기
    def get(self, request):
        my_collection = CollectionModel.objects.filter(owner_id=request.user.id).order_by('-id')
        # print(my_collection)
        serializers_data = CollectionSerializer(my_collection, many=True).data
        # print(serializers_data)
        return Response(serializers_data)
    def post(self, request):
        return Response()
    def put(self, request):
        return Response()
    def delete(self, request):
        return Response()
