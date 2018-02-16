from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from modules.book import service as book_sv
from modules.memo import service as memo_sv, forms as memo_form
from submodules.helper import flatten_dict_only_one_element as flatten
from django.contrib import messages
from ..urls import app_name


@require_GET
def get(request, book_pk):
    return render(request, app_name + '/new.html',
                  {'form': memo_form.NewMemo,
                   'hidden': {'book_pk': book_pk}})


@require_POST
def post(request, book_pk):
    """メモをする"""
    user, data = request.user, flatten(request.POST)

    if memo_sv.post_memo(user, book_sv.get_book(book_pk), data['text']):
        messages.success(request, 'メモをしました!')

    return redirect('books:detail', pk=book_pk)
