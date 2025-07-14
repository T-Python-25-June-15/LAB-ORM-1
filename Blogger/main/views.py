from django.shortcuts import render, redirect
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-published_at')
    return render(request, 'main/home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Post.objects.create(title=title, content=content, is_published=True)
            return redirect('home')
    return render(request, 'main/add_post.html')
