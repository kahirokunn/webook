from django.urls import path
from .views import index, generate

app_name = 'books'

urlpatterns = [
    path('', index.routing_by_request_method, name='index'),
    path('/generate', generate.routing_by_request_method, name='generate'),
]
