from django.conf.urls import url
from . import views
from constants import ROOT_NAME

app_name = 'index'

urlpatterns = [
    url(r'^$', views.dashboard, name=ROOT_NAME),
]
