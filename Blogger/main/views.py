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

def detail_views(request:HttpRequest, blog_id:int):
    blog = Post.objects.get(pk=blog_id)
    return render(request, 'main/blog_details.html', {"blog":blog})


def update_views(request:HttpRequest, blog_id:int):
    blog = Post.objects.get(pk=blog_id)
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.published_at = request.POST["published_at"]
        if "images" in request.FILES:
            blog.images = request.FILES["images"]
        blog.save()
        return redirect('main:detail_views', blog_id = blog.id)

    return render(request, 'main/update.html', {"blog":blog})

def delete_views(request:HttpRequest, blog_id:int):
    blog = Post.objects.get(pk=blog_id)
    blog.delete()
    return redirect('main:home_views')
