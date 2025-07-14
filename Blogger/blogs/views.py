from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.utils import timezone
from .models import Blog

# Create your views here.



def createBlogs_view(request:HttpRequest):

    if request.method =="POST":
        published_at_raw = request.POST.get("published_at")
        published_at = published_at_raw if published_at_raw else timezone.now().date()

        new_blog=Blog(title=request.POST["title"],content=request.POST["content"],is_published = "is_published" in request.POST, published_at=published_at,)

        if "image" in request.FILES:
            new_blog.image = request.FILES["image"]

        new_blog.save()
        return redirect('main:home_view')
    return render(request, "blogs/createBlogs.html")


def detailBlog_view(request:HttpRequest,blog_id:int):
    blog= Blog.objects.get(pk=blog_id)

    return render(request, "blogs/detailBlog.html",{"blog":blog} )


def updateBlog_view(request:HttpRequest,blog_id:int):
    blog= Blog.objects.get(pk=blog_id)

    if request.method =="POST":
        blog.title=request.POST["title"]
        blog.content=request.POST["content"]
        blog.is_published = "is_published" in request.POST
        blog.published_at=request.POST["published_at"]
        if "image" in request.FILES: blog.image= request.FILES["image"]
        blog.save()

        return redirect("blogs:detailBlog_view", blog_id=blog.id)

    return render(request, "blogs/updateBlog.html",{"blog":blog} )

def deleteBlog_view(request:HttpRequest,blog_id:int):
    blog= Blog.objects.get(pk=blog_id)
    blog.delete()

    return redirect('main:home_view')

