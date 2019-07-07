from django.conf.urls import url
from gallery import views


urlpatterns = [
    url(r'^$', views.redirect, name='redirect'),
    url(r'^([0-9]+)/$', views.Main.as_view(), name='main'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]


