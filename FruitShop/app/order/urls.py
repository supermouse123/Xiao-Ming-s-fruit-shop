from django.conf.urls import url, include
from order.views import OrderPlaceView, OrderCommitView

urlpatterns = [
    url(r'^place', OrderPlaceView.as_view(), name='place'),
    url(r'^commit', OrderCommitView.as_view(), name='commit'),

]
