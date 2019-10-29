from django.conf.urls import url
from cart import views
urlpatterns = [
    url(r"^index/$", views.index),
    url(r"^select_goods/$", views.select_goods),
    ]