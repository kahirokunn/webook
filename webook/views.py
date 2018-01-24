from django.shortcuts import render
from webook.models import Post


def post_list(request):
    posts = Post.published_list()
    return render(request, 'webook/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'webook/post_detail.html', {'post': post})
