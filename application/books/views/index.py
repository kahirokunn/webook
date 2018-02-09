from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from submodules.helper import get_logger
from submodules.decorators import valid_request_method

logger = get_logger()


@require_http_methods('GET')
def get(request):
    get_logger().debug(request.GET)
    return render(request, 'books/index.html')


@valid_request_method('GET')
def routing_by_request_method(request):
    """許可されたmethodを自動で呼ぶ"""
    return eval(request.method.lower())(request)
