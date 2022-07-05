from rest_framework import  serializers
from .models import Post as PostModel
from .models import Collection as CollectionModel
from user.models import User as UserModel     
from .model_run import model_run, control_s3

import boto3
# from .views import ModelView
# from .views import control_s3

class PostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        print(f"이즈마인 제대로 나와라 죽어진짜->{validated_data}")
        validated_data.pop('like')
        userid = 1
        validated_data['image']._set_name("input.jpg")
        post = PostModel.objects.create(**validated_data)
        run_model = model_run()
        styled_image = 'media/uploads/result.jpeg'  
        url = control_s3(styled_image, userid)
        post.artimage = url
        post.save()
        
        print(f"post.id->{post.id}")
        print(f"post.artist->{post.artist}")
        upload_collection = CollectionModel.objects.create(post=post, owner=post.artist)

        target_owner = UserModel.objects.get(id=post.artist.id)
        print(f"사용자는 누구? ->{target_owner}")
        target_owner.point = target_owner.point + 3
        target_owner.save()
        print(f"포인트 세이브? ->{target_owner.point}")
        
        return post

    artist_name = serializers.SerializerMethodField()
    def get_artist_name(self, obj):
        return obj.artist.nickname
    class Meta:
        model = PostModel
        fields = "__all__"
        
        
    
    
class CollectionSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    owner_names = serializers.SerializerMethodField()
    def get_owner_names(self, obj):
        return obj.owner.nickname
        

    class Meta:
        model = CollectionModel
        fields = "__all__"
    