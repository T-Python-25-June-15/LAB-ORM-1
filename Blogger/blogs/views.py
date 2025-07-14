from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.utils import timezone
from .models import Blog

# Create your views here.



def createBlogs_view(request:HttpRequest):



    if request.method =="POST":
        published_at_raw = request.POST.get("published_at")
        published_at = published_at_raw if published_at_raw else timezone.now().date()


        new_blog=Blog(title=request.POST["title"],content=request.POST["content"],is_published = "is_published" in request.POST, published_at=published_at)
        new_blog.save()



    return render(request, "blogs/createBlogs.html")

