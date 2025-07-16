from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Post

# Create your views here.
def create_posts(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content)
        return redirect("main:home_view")  # after creation, go back home

    return render(request, "posts/create.html")


