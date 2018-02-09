from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from constants import ROOT_NAME

urlpatterns = [
    url('', include('index.urls'), name=ROOT_NAME),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
]
