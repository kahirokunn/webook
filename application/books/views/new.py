from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib import messages
from modules.orderbook.forms import NewOrder
from modules.orderbook import service as orderbook_sv
from submodules.helper import flatten_dict_only_one_element as flatten, \
    simple_upload_file
from ..urls import app_name


@require_GET
def get(request):
    return render(request, app_name + '/new.html', {'form': NewOrder})


@require_POST
def post(request):
    """新たらしい本を購入する"""
    data = flatten(request.POST)
    data['price'] = int(data['price'])
    if not orderbook_sv.is_money_sufficient(request.user, data['price']):
        messages.warning(request, '予算が足りません')
        return redirect(app_name + ':index')

    if 'thumbnail_url' in request.FILES:
        data['thumbnail_url'] = simple_upload_file(
            request.FILES['thumbnail_url'])

    orderbook = orderbook_sv.order_new_one(request.user,
                                           data,
                                           int(data['price']),
                                           data['ordered_at'])
    if orderbook is not None:
        messages.success(request, '本を購入しました')
        return redirect(app_name + ':detail', pk=orderbook.book.pk)
    else:
        messages.warning(request, '新規購入しようとした本は既に存在しています。\
        同じ本を購入したい場合は対象の本の詳細画面から購入してください。')
        return redirect(app_name + ':index')
