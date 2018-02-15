from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from modules.book.forms import NewCategory
from modules.book import service as book_sv
from submodules.helper import flatten_dict_only_one_element as flatten
from django.contrib import messages


@require_GET
def get(request):
    return render(request, 'categories/new.html', {'form': NewCategory})


@require_POST
def post(request):
    """新たらしい本を購入する"""
    data = flatten(request.POST)
    if book_sv.new_category(data['name']):
        msg = '新しいカテゴリ {0} を追加しました'.format(data['name'])
    else:
        msg = '入力したカテゴリ {0} は既に登録されています'.format(data['name'])
    messages.success(request, msg)

    return redirect('categories:new')
