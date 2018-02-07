from .models import Books
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from application.helper import Log


def home(request):
    Log.info(request.user.is_authenticated)
    return render(request, 'webook/home/index.html')
