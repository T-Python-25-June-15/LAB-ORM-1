from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone


def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'main/home.html', {'posts': posts})


def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = 'is_published' in request.POST

        Post.objects.create(
            title=title,
            content=content,
            is_published=is_published,
            published_at=timezone.now()
        )

        return redirect('home')

    return render(request, 'main/add_post.html')