from django.shortcuts import render
from webook.models import Post
from webook.forms import PostForm
from django.shortcuts import redirect


def home(request):
    return render(request, 'webook/home/index.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'webook/books/index.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'webook/books/detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = PostForm()
    return render(request, 'webook/books/create.html', {'form': form})
