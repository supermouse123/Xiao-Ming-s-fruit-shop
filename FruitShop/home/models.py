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


#总体介绍模型
class Nav(Common):
    class Meta:
        db_table = "fruit_nav"


#时令水果模型
class Seasonal_Fruits(Common):
    class Meta:
        db_table = "fruit_seasonal"


#VC季模型
class VC(Common):
    class Meta:
        db_table = "fruit_vc"


#海鲜模型
class SeaFood(Common):
    class Meta:
        db_table = "seafood"


#主页的商品模型
class MainShop(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)
    price = models.CharField(max_length=30)
    class Meta:
        db_table = "fruit_mainshop"


















