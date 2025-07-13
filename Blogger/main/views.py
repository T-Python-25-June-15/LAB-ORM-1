from django.shortcuts import render, redirect
from .models import Post
# Create your views here.


def home_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'main/index.html',  context)


def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = request.POST.get('is_published') == 'on'

        Post.objects.create(
            title=title,
            content=content,
            is_published=is_published
        )
        return redirect('/')

    return render(request, 'main/add_post.html')