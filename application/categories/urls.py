from django.urls import path
from submodules.helper import ViewRouter

app_name = 'categories'

route = ViewRouter(app_name=app_name)

urlpatterns = [
    # 新規登録画面
    path('new', route.new, name='new'),
]
