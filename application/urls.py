from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from django.views.static import serve
from django.views.i18n import null_javascript_catalog
import settings
from constants import ROOT_NAME
from submodules.helper import get_urls
from index import urls as index_urls
from accounts import urls as account_urls
from books import urls as book_urls
from categories import urls as category_urls
from reviews import urls as review_urls

urlpatterns = [
    url('', get_urls(index_urls)),
    path('admin/', admin.site.urls),
    path('accounts/', get_urls(account_urls)),
    path('books/', get_urls(book_urls)),
    path('categories/', get_urls(category_urls)),
    path('reviews/', get_urls(review_urls)),

    # assets
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    url('i18n_js_catalog', null_javascript_catalog, name='i18n_js_catalog'),
]
