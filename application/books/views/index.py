from django.shortcuts import render
from django.views.decorators.http import require_GET
from modules.book import service as book_sv
from ..urls import app_name


@require_GET
def get(request):
    return render(request, app_name + '/index.html',
                  {'posts': book_sv.get_books()})
