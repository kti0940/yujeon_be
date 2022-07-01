from rest_framework import  serializers
from .models import Post as PostModel
from user.models import User as UserModel     

class PostSerializer(serializers.ModelSerializer):
    artist_name = serializers.SerializerMethodField()
    def get_artist_name(self, obj):
        return obj.artist.nickname

    class Meta:
        model = PostModel
        fields = "__all__"