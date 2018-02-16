from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from modules.book.forms import NewCategory
from modules.book import service as book_sv
from submodules.helper import flatten_dict_only_one_element as flatten
from django.contrib import messages
from ..urls import app_name


@require_GET
def get(request):
    return render(request, app_name + '/new.html', {'form': NewCategory})


@require_POST
def post(request):
    """新たらしいカテゴリを追加する"""
    data = flatten(request.POST)
    if book_sv.new_category(data['name']):
        messages.success(request, '新しいカテゴリ {0} を追加しました'.format(data['name']))
    else:
        messages.warning(request,
                         '入力したカテゴリ {0} は既に登録されています'.format(data['name']),
                         extra_tags='danger')

    return redirect(app_name + ':new')
