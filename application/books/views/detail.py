from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from modules.book import service as book_sv


@require_http_methods('GET')
def get(request, pk):
    book = book_sv.get_book(pk)
    return render(request, 'books/detail.html',
                  {'post': book, 'categories': book.categories.all()})


@require_http_methods('PUT')
def post(request):
    return render(request, 'books/new.html')
