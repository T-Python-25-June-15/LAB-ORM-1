from django.shortcuts import render, redirect
from .models import Post
from datetime import datetime
from django.contrib import messages

def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = request.POST.get('is_published') == 'on'

        Post.objects.create(
            title=title,
            content=content,
            is_published=is_published,
            published_at=datetime.now()
        )
        messages.success(request, "The post was added successfully")

        return redirect('blog:home')

    return render(request, 'blog/add_post.html')
