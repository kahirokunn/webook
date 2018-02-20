from django.urls import path
from submodules.helper import ViewRouter

app_name = 'orderhistories'

route = ViewRouter(app_name=app_name)

urlpatterns = [
    # 一覧画面
    path('', route.index, name='index'),
]
