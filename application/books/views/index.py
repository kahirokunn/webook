from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from submodules import logger
from submodules.decorators import valid_request_methods
from modules.book.service import get_books


@require_http_methods('GET')
def get(request):
    logger.info(get_books())
    return render(request, 'books/index.html', {'posts': get_books()})


@valid_request_methods('GET')
def routing_by_request_method(request):
    """許可されたmethodを自動で呼ぶ"""
    return eval(request.method.lower())(request)
