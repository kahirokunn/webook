from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib import messages
from modules.orderbook.forms import NewOrder
from modules.orderbook import service as orderbook_sv
from submodules.helper import flatten_dict_only_one_element as flatten
from ..urls import app_name


@require_GET
def get(request):
    return render(request, app_name + '/new.html', {'form': NewOrder})


@require_POST
def post(request):
    """新たらしい本を購入する"""
    data = flatten(request.POST)
    orderbook = orderbook_sv.order_new_one(request.user,
                                           data,
                                           int(data['price']),
                                           data['ordered_at'])
    messages.success(request, '本を購入しました')
    return redirect(app_name + ':detail', pk=orderbook.book.pk)
