from submodules.decorators import valid_attr_or_failed


@valid_attr_or_failed('urlpatterns', 'app_name')
def get_urls(module):
    valid_attr_or_failed(module, 'urlpatterns', 'app_name')
    urlpatterns = getattr(module, 'urlpatterns')
    app_name = getattr(module, 'app_name')
    return urlpatterns, app_name, app_name
