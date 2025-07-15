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
        image = request.FILES.get('image','')

        post = Post.objects.create(
            title=title,
            content=content,
            published_at=timezone.now(),
            is_published=True,
            image=image
        )
        return redirect('home')
    
    return render(request, 'blog/add_post.html')


def post_detail(request:HttpRequest, post_id:int):
    post = Post.objects.get(pk=post_id)

    return render(request, 'blog/post_detail.html',{"post": post})

def post_update(request:HttpRequest, post_id:int):
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        if "image" in request.FILES: post.image = request.FILES["image"]
        post.save()
        return redirect('post_detail',post_id=post.id)


    return render(request, 'blog/post_update.html',{"post": post})

def post_delete(request:HttpRequest, post_id:int):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('home')