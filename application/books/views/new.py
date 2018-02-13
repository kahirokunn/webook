from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, \
    require_POST
from submodules.decorators import valid_request_methods
from modules.order_book.forms import NewForm
from modules.order_book.service import order_new_one
from modules.book.service import new_book, get_book_fields
from submodules.helper import flatten_dict_only_one_element
from typing import Iterable


@require_GET
def get(request):
    return render(request, 'books/new.html', {'form': NewForm})


@require_POST
def post(request):
    """新たらしい本を購入する"""
    data = flatten_dict_only_one_element(request.POST)
    order_new_one(request.user, data, int(data['price']),
                  data['ordered_at'])
    return render(request, 'books/new.html', {'form': NewForm})


@valid_request_methods(['GET', 'POST'])
def routing_by_request_method(request):
    """許可されたmethodを自動で呼ぶ"""
    return eval(request.method.lower())(request)
