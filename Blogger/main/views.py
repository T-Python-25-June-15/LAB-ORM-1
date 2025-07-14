from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.

def home_views(request:HttpRequest):
    posts = Post.objects.all()
    return render(request, 'main/home_page.html', {'posts':posts})

def add_blog_views(request:HttpRequest):
    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content=request.POST["content"], published_at=request.POST["published_at"], images=request.FILES["images"])
        new_post.save()
        return redirect('main:home_views')
    return render(request, 'main/add_page.html')
