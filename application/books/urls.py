from django.urls import path
from .views import index, new, detail

app_name = 'books'

urlpatterns = [
    # 一覧画面
    path('', index.routing_by_request_method, name='index'),

    # 詳細画面
    path('<int:pk>', detail.routing_by_request_method, name='detail'),

    # 新規登録画面
    path('new', new.routing_by_request_method, name='new'),
]
