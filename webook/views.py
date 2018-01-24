from django.shortcuts import render
from webook.models import Post


def post_list(request):
    posts = Post.published_list()
    return render(request, 'webook/post_list.html', {'posts': posts})
