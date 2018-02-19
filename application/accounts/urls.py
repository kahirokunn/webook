from django.urls import path
from django.conf.urls import include
from submodules.helper import ViewRouter
from . import views

app_name = 'accounts'

route = ViewRouter(app_name=app_name)

urlpatterns = [
    path('update/self', route.update, name='update'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls'), name='accounts'),
]
