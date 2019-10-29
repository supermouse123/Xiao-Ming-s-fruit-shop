from django.conf.urls import url
from classify import views
urlpatterns = [
    url(r"^index/$", views.index),
    url(r"^index/(\d+)/(\d+)/(\d+)/$", views.index)
    ]