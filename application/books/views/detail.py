from django.shortcuts import render
from django.views.decorators.http import require_GET
from modules.book import service as book_sv
from modules.review import service as review_sv
from modules.memo import service as memo_sv
from ..urls import app_name


@require_GET
def get(request, pk):
    book = book_sv.get_book(pk)
    reviews = review_sv.get_reviews_separate_user(request.user, book)
    memos = memo_sv.get_memos_separate_user(request.user, book)
    return render(request, app_name + '/detail.html',
                  {'post': book,
                   'categories': book.categories.all(),
                   'is_reviewed': review_sv.is_reviewed(request.user, book),
                   'my_review': reviews['target_review'],
                   'reviews': reviews['reviews'],
                   'my_memos': memos['target_memos'],
                   'memos': memos['memos'], })
