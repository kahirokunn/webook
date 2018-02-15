from django.shortcuts import render
from django.views.decorators.http import require_GET
from modules.book import service as book_sv
from ..urls import app_name


@require_GET
def get(request, pk):
    book = book_sv.get_book(pk)
    reviews = book_sv.get_reviews_separate_user(request.user, book)
    return render(request, app_name + '/detail.html',
                  {'post': book,
                   'categories': book.categories.all(),
                   'is_reviewed': book_sv.is_reviewed(request.user, book),
                   'my_review': reviews['target_review'],
                   'reviews': reviews['reviews'], })
