from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^sign-up/$', views.signing_up, name='signing_up'),
    url(r'^sign-in/$', views.signing_in, name='signing_in'),
    url(r'^sign-out/$', auth_views.LogoutView.as_view(),{"next_page": "/"}, name='signing_out'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate_account'),
    url(r'^wrong-credentials/$', views.wrong_credentials, name='wrong_credentials'),
]