from django.shortcuts import render
from django.views.decorators.http import require_GET
from modules.orderbook import service as orderbook_sv
from ..urls import app_name


@require_GET
def get(request):
    return render(request, app_name + '/index.html',
                  {'posts': orderbook_sv.get_orderbook()})
