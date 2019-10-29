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


class ClassifyList(models.Model):
    typeid = models.CharField(max_length=100)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=300)
    class Meta:
        db_table = "classifylist"


class AllGoods(models.Model):
    productid = models.CharField(max_length=10)         #商品id
    productimg = models.CharField(max_length=150)       #商品图片
    productname = models.CharField(max_length=200)      #商品名字
    isxf = models.NullBooleanField(default=False)       #是否是精选
    specifics = models.CharField(max_length=30)         #规格
    price = models.CharField(max_length=10)             #价格
    categoryid = models.CharField(max_length=10)        #组id  例如：热销榜
    childcid = models.CharField(max_length=10)          #子类组id  例如：进口水果
    dealerid = models.CharField(max_length=10)          #详情页id
    storenums = models.IntegerField()                   #库存
    productnum = models.IntegerField()                  #销量
    class Meta:
        db_table = "fruit_allgoods"

    def __str__(self):
        return self.categoryid




















