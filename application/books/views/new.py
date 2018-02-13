from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from submodules import logger
from submodules.decorators import valid_request_methods
from modules.order_book.forms import NewForm


@require_http_methods('GET')
def get(request):
    logger.info(request.GET)
    return render(request, 'books/new.html', {'form': NewForm})


@require_http_methods('POST')
def post(request):
    logger.info(request.POST)
    return render(request, 'books/new.html')


@valid_request_methods(['GET', 'POST'])
def routing_by_request_method(request):
    """許可されたmethodを自動で呼ぶ"""
    return eval(request.method.lower())(request)
