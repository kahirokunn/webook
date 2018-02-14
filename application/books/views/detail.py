from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from modules.book.service import get_book


@require_http_methods('GET')
def get(request, pk):
    book = get_book(pk)
    return render(request, 'books/detail.html',
                  {'post': book, 'categories': book.categories.all()})


@require_http_methods('PUT')
def post(request):
    return render(request, 'books/new.html')
