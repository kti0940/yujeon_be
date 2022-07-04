from django.db import models
from django.forms import DateTimeField
from user.models import User
        
class Post(models.Model):
    artist = models.ForeignKey('user.User',verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    image = models.ImageField(upload_to='uploads')
    artimage = models.URLField("유화이미지", max_length=200, default='')
    desc = models.TextField("작품설명")
    cost = models.IntegerField("가격", default=3)
    is_mine = models.BooleanField(default=True)
    like = models.ManyToManyField(User, related_name='좋아요', blank=True)
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    is_exposure = models.BooleanField(default=True)
    on_sale = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Collection(models.Model):
    owner = models.ForeignKey('user.User', verbose_name="소유자", on_delete=models.CASCADE)
    post = models.ForeignKey('post.Post', verbose_name="게시글", on_delete=models.CASCADE)
    