from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Post

# Create your views here.

def create_post_view(request: HttpRequest):

    if request.method == "POST":
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
            is_published = request.POST.get("is_published") == "on",
            published_at= datetime.now()
        )
        new_post.save()

    return render(request, "blog/create.html")

def delete_all_objects_view(request: HttpRequest):
    Post.objects.all().delete() 

    return render(request, "blog/create.html")
