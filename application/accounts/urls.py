from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls'), name='accounts'),
]
