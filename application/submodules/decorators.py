from django.http import HttpResponseNotAllowed
from submodules.constants import REQUEST_METHOD_LIST
from functools import wraps


def valid_request_method(request_method_list=REQUEST_METHOD_LIST):
    """許可されたrequest methodか判定する"""

    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            if request.method not in request_method_list:
                logger.warning(
                    'Method Not Allowed (%s): %s', request.method,
                    request.path,
                    extra={'status_code': 405, 'request': request}
                )
                return HttpResponseNotAllowed(request_method_list)
            return func(request, *args, **kwargs)

        return inner

    return decorator
