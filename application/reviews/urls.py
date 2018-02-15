from django.urls import path
from submodules.helper import ViewRouter

app_name = 'reviews'

route = ViewRouter(app_name=app_name)

urlpatterns = [
    # 新規投稿画面
    path('new/<int:book_pk>', route.new, name='new'),
]
