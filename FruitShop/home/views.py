from django.shortcuts import render, HttpResponse
from home.models import *
# Create your views here.

def index(request):
    wheelsList = Wheel.objects.all()
    navList = Nav.objects.all()
    seasonalList = Seasonal_Fruits.objects.all()
    vcList = VC.objects.all()
    seafood = SeaFood.objects.all()
    seasonal_list = MainShop.objects.filter(trackid="21871")
    vc_list = MainShop.objects.filter(trackid="21873")
    sea_list = MainShop.objects.filter(trackid="21874")

    # print(wheelsList[0].img)
    print(seasonal_list)
    print(vc_list)
    return render(request, "home.html", {"wheelsList": wheelsList, "navList": navList, "seasonalList": seasonalList,
                                         "vcList": vcList, "seafood": seafood, "seasonal_list": seasonal_list,
                                         "vc_list": vc_list, "sea_list": sea_list})