import json
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from submodules import logger
from submodules.decorators import valid_request_methods
from modules.book.service import get_book


@require_http_methods('GET')
def get(request, pk):
    return render(request, 'books/detail.html', {'post': get_book(pk)})


@require_http_methods('PUT')
def post(request):
    logger.info(request.POST)
    return render(request, 'books/create.html')


@valid_request_methods(['GET', 'PUT'])
def routing_by_request_method(request, **kwargs):
    """許可されたmethodを自動で呼ぶ"""
    return eval(request.method.lower())(request, **kwargs)
