from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


#定义父类模型
class Common(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=10)
    class Meta:
        abstract = True


#轮播图模型
class Wheel(Common):
    class Meta:
        db_table = "fruit_wheel"


#每日必抢模型
class Nav(Common):
    class Meta:
        db_table = "fruit_nav"


#必买模型
class MustBuy(Common):
    class Meta:
        db_table = "fruit_mustbuy"


#首页下的商品模型
class Shop(Common):
    class Meta:
        db_table = "fruit_shop"


















