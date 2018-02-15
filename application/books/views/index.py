from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from modules.book import service as book_sv


@require_http_methods('GET')
def get(request):
    return render(request, 'books/index.html', {'posts': book_sv.get_books()})
