from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post  
from django.utils import timezone

def home_view(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.filter(is_published=True).order_by('-published_at')


    return render(request, "main/home_view.html", {"posts": posts})

def add_post_view(request: HttpRequest) -> HttpResponse:


    if request.method == "POST":

        
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
        )



        new_post.save()



        return redirect("home_view")
    

    return render(request, "main/add_post_view.html")

