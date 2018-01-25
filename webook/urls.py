from django.conf.urls import url
from webook import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
