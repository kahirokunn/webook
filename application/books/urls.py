from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.routing_by_request_method, name='signup'),
]
