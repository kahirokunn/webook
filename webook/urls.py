from django.conf.urls import include, url
from webook import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)$', views.post_detail, name='post_detail'),
    url(r'^post/new$', views.post_new, name='post_new'),
]
