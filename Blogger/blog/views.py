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
        image = request.FILES.get('image')
        Post.objects.create(
            title=title,
            content=content,
            is_published=is_published,
            published_at=datetime.now()
        )
        messages.success(request, "The post was added successfully")

        return redirect('blog:home')

    return render(request, 'blog/add_post.html')

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_published = request.POST.get('is_published') == 'on'
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        post.save()
        messages.success(request, "Post updated successfully ✅")
        return redirect('blog:post_detail', post_id=post.id)

    return render(request, 'blog/edit_post.html', {'post': post})

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    messages.success(request, "Post deleted 🗑️")
    return redirect('blog:home')
