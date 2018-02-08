from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    url(r'', include('application.index.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('application.accounts.urls')),
    path('books/', include('application.books.urls')),
]
