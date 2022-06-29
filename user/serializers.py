from rest_framework import serializers

from user.models import User as UserModel

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
        
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user
    
    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user