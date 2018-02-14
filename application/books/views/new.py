from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from modules.order_book.forms import NewForm
from modules.order_book.service import order_new_one
from submodules.helper import flatten_dict_only_one_element as flatten


@require_GET
def get(request):
    return render(request, 'books/new.html', {'form': NewForm})


@require_POST
def post(request):
    """新たらしい本を購入する"""
    data = flatten(request.POST)
    orderbook = order_new_one(request.user, data, int(data['price']),
                              data['ordered_at'])
    return redirect('books:detail', pk=orderbook.book.pk)
