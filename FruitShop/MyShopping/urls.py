from django.conf.urls import url
from MyShopping import views
urlpatterns = [
    url(r"^index/$", views.index)
    ]