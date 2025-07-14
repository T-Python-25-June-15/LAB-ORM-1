from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

def home_view(request:HttpRequest):
    posts = Post.objects.all()
    return render(request,"main/index.html",{"posts":posts})

def add_post(request:HttpRequest):
    if request.method == "POST" and "image" in  request.FILES:
        new_post = Post(title = request.POST["title"], content = request.POST["content"], image = request.FILES["image"])
        new_post.save()
        return redirect("main:home_view")
    elif request.method == "POST" and "image" not in request.FILES:
        new_post = Post(title = request.POST["title"], content = request.POST["content"])
        new_post.save()
        return redirect("main:home_view")
    return render(request,"main/add_post.html")

def detail_post_view(request:HttpRequest, post_id:int):
    post = Post.objects.get(id = post_id)
    return render(request,"main/detail_post.html", {"post" : post})

def update_post_view(request:HttpRequest, post_id:int):
    post = Post.objects.get(id = post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        if "image" in  request.FILES:
            post.image = request.FILES["image"]
        post.save()
        return redirect("main:detail_post_view", post_id=post.id)
    return render(request,"main/update_post.html", {"post" : post})

def delete_post_view(request:HttpRequest, post_id:int):
    post = Post.objects.get(id = post_id)
    post.delete()
    return redirect("main:home_view")
