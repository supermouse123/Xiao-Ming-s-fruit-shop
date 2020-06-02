from django.conf.urls import url, include
from cart.views import CartAddView, CartInfoView, CartUpdateView, CartDetleView


urlpatterns = [
    url(r'^add$', CartAddView.as_view(), name='add'),
    url(r'^$', CartInfoView.as_view(), name='show'),
    url(r'^update$', CartUpdateView.as_view(), name='update'),
    url(r'^delete', CartDetleView.as_view(), name='delete'),
]
