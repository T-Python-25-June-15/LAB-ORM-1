from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from .models import Post

# Create your views here.

def home(request:HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/home.html', {'posts': posts})

def add_post(request:HttpRequest):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        
        post = Post.objects.create(
            title=title,
            content=content,
            published_at=timezone.now(),
            is_published=True
        )
        return redirect('home')
    
    return render(request, 'blog/add_post.html')
