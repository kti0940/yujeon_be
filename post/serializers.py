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
        validated_data.pop('like')
        userid = 1
        validated_data['image']._set_name("input.jpg")
        post = PostModel.objects.create(**validated_data)
        model_run()
        styled_image = 'media/uploads/result.jpeg'  
        url = control_s3(styled_image, userid)
        post.artimage = url
        post.save()
        
        CollectionModel.objects.create(post=post, owner=post.artist)

        target_owner = UserModel.objects.get(id=post.artist.id)
        target_owner.point = target_owner.point + 3
        target_owner.save()
        
        return post

    artist_name = serializers.SerializerMethodField()
    def get_artist_name(self, obj):
        return obj.artist.nickname
    
    collection_id = serializers.SerializerMethodField()
    def get_collection_id(self, obj):
        return obj.collection.id
    
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
    