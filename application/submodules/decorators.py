import json
from functools import wraps
from django.http import HttpResponseNotAllowed
from .constants import REQUEST_METHOD_LIST
from submodules import logger


def valid_request_methods(request_method_list=REQUEST_METHOD_LIST):
    """許可されたrequest methodか判定する"""

    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            if request.method not in request_method_list:
                logger.warning(
                    'Method Not Allowed ({0}): {1}'.format(request.method,
                                                           request.path))
                return HttpResponseNotAllowed(request_method_list)
            return func(request, *args, **kwargs)

        return inner

    return decorator


def get_no_attr_list(module, *attrs) -> list:
    """モジュールにない属性一覧を取得"""
    no_attrs = []
    for attr in attrs:
        if not hasattr(module, attr):
            no_attrs.append(attr)
    return no_attrs


def valid_attr_or_failed(*attrs):
    """モジュールにない属性があったら例外を出す"""

    def decorator(func):
        @wraps(func)
        def inner(module, *args, **kwargs):
            no_attr_list = get_no_attr_list(module, *attrs)
            if len(no_attr_list) > 0:
                msg = 'required attr **{0}** is not defined in {1} module.'
                raise Exception(
                    msg.format(json.dumps(no_attr_list), module.__name__))
            return func(module, *args, **kwargs)

        return inner

    return decorator
