from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

def home_view(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, "blog/index.html", context={"posts" : posts})

def add_post(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        new_post = Post(
            title=title,
            content=content,
            is_published=True  
        )
        new_post.save()
        return redirect("blog:home_view")
    
    return render(request, "blog/addPost.html")



