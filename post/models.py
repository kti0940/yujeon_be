from django.db import models
from django.forms import DateTimeField

# Create your models here.
class Post(models.Model):
    artist = models.ForeignKey('user.User',verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    image = models.ImageField(upload_to='uploads')
    artimage = models.URLField("유화이미지", max_length=200, default='')
    desc = models.TextField("작품설명")
    cost = models.IntegerField("가격")
    is_mine = models.BooleanField(default=True)
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    
    def __str__(self):
        return self.title
