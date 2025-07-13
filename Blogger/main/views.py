from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.

def home_views(request:HttpRequest):
    posts = Post.objects.all()
    return render(request, 'main/home_page.html', {'posts':posts})

def add_blog_views(request:HttpRequest):
    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content=request.POST["content"], published_at=request.POST["published_at"])
        new_post.save()
    return render(request, 'main/add_page.html')
