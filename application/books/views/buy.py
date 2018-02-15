from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib import messages
from modules.orderbook import service as orderbook_sv
from modules.book import service as book_sv
from modules.orderbook.forms import Order
from submodules.helper import flatten_dict_only_one_element as flatten
from ..urls import app_name


@require_GET
def get(request, pk):
    return render(request, app_name + '/new.html',
                  {'form': Order})


@require_POST
def post(request, pk):
    """登録されている本を購入する"""
    data = flatten(request.POST)

    orderbook = orderbook_sv.order_existing_one(request.user,
                                                book_sv.get_book(pk),
                                                int(data['price']),
                                                data['ordered_at'])
    messages.success(request, '本を購入しました！')

    return redirect(app_name + ':detail', pk=orderbook.book.pk)
