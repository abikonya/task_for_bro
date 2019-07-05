from django.conf.urls import url
from gallery import views


urlpatterns = [
    url(r'^$', views.Main.as_view(), name='main'),
]


