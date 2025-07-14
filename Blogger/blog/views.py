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
            published_at= datetime.now(),
            image=request.FILES["image"]
        )
        new_post.save()
        return redirect('main:home_view')
    
    return render(request, "blog/create.html")

def blog_update_view(request: HttpRequest, blog_id: int):

    blog = Post.objects.get(pk=blog_id)

    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST.get("is_published") == "on"
        blog.published_at = datetime.now()
        
        if "image" in request.FILES : blog.image = request.FILES["image"]
        
        
        blog.save()
        
        
        
        
        return redirect('blog:blog_detail_view' , blog_id = blog.id)
    
    return render(request, "blog/blog_update.html", {"blog": blog})



def delete_all_objects_view(request: HttpRequest):
    Post.objects.all().delete() 

    return render(request, "blog/create.html")

def delete_blog_view(request: HttpRequest , blog_id: int):

    blog = Post.objects.get(pk=blog_id)

    blog.delete()
    return redirect('main:home_view')



def blog_detail_view(request: HttpRequest , blog_id :int):
     
    blog = Post.objects.get(pk=blog_id)
    print(blog.title)
    return render(request, "blog/blog_detail.html", {"blog" : blog})
