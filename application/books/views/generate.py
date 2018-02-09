from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from submodules import logger
from submodules.decorators import valid_request_methods


@require_http_methods('GET')
def get(request):
    logger.debug(request.GET)
    return render(request, 'books/index.html')


@require_http_methods('POST')
def post(request):
    logger.debug(request.POST)
    return render(request, 'books/create.html')


@valid_request_methods(['GET', 'POST'])
def routing_by_request_method(request):
    """許可されたmethodを自動で呼ぶ"""
    return eval(request.method.lower())(request)
