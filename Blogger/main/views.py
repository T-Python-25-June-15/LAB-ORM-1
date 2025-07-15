from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

def home_view(request:HttpRequest):
    posts = Post.objects.all()
    return render(request,"main/index.html",{"posts":posts})

def add_post(request:HttpRequest):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        is_published = 1 if "publish" in request.POST else 0

        if "image" in request.FILES:
            new_post = Post(title=title, content=content, is_published=is_published, image=request.FILES["image"],)
        else:
            new_post = Post(title=title, content=content, is_published=is_published)
        print(request.POST)
        new_post.save()
        return redirect("main:home_view")

    return render(request, "main/add_post.html")

def detail_post_view(request:HttpRequest, post_id:int):
    post = Post.objects.get(id = post_id)
    return render(request,"main/detail_post.html", {"post" : post})

def update_post_view(request:HttpRequest, post_id:int):
    post = Post.objects.get(id = post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.is_published = 1 if "publish" in request.POST else 0
        if "image" in  request.FILES:
            post.image = request.FILES["image"]
        post.save()
        return redirect("main:detail_post_view", post_id=post.id)
    return render(request,"main/update_post.html", {"post" : post})

def delete_post_view(request:HttpRequest, post_id:int):
    post = Post.objects.get(id = post_id)
    post.delete()
    return redirect("main:home_view")

def all_posts_view(request:HttpRequest):
    posts = Post.objects.all()
    return render(request,"main/all_posts.html",{"posts":posts})