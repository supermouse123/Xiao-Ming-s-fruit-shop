from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from user.views import RegisterView, ActiveView, LoginView, UserInfoView, UserOrderView, AddressView, LogoutView

urlpatterns = [
    url(r'^register$', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    # url(r'^$', login_required(UserInfoView.as_view()), name='user'),
    # url(r'^order$', login_required(UserOrderView.as_view()), name='order'),
    # url(r'^address$', login_required(AddressView.as_view()), name='address'),
    url(r'^$', UserInfoView.as_view(), name='user'),
    url(r'^order$', UserOrderView.as_view(), name='order'),
    url(r'^address$', AddressView.as_view(), name='address'),

    url(r'^order/(?P<page>\d+)$', UserOrderView.as_view(), name='order'),
]
