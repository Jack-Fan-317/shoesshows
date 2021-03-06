from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 模型类
class Product(models.Model):
    # 表字段
    title = models.CharField(default="例：AJ1", max_length=50)
    intro = models.TextField(default="在这里写球鞋介绍")
    icon = models.ImageField(default="default_icon.png",upload_to='images/') 
    image = models.ImageField(default="default_image.png",upload_to='images/')
    
    votes = models.IntegerField(default=1)
    pub_date = models.DateTimeField()
    publish_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 后台显示的model名称
    def __str__(self):
        return self.title