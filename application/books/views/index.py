from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from modules.book.service import get_books


@require_http_methods('GET')
def get(request):
    return render(request, 'books/index.html', {'posts': get_books()})
