from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from submodules.helper import get_logger
from submodules.decorators import valid_request_method


@require_http_methods('GET')
def get(request):
    return render(request, 'index/index.html')


@require_http_methods('POST')
def post(request):
    pass


@require_http_methods('PUT')
def put(request):
    pass


@require_http_methods('DELETE')
def delete(request):
    pass


@valid_request_method
def routing_by_request_method(request):
    """許可されたmethodを自動で呼ぶ"""
    return eval(request.method.lower())(request)
