from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.http import HttpRequest


def home(request: HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'main/home.html', {'posts': posts})


def add_post(request: HttpRequest):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = 'is_published' in request.POST
        poster = request.FILES.get('poster')

        if poster:
            
            Post.objects.create(
                title=title,
                content=content,
                is_published=is_published,
                published_at=timezone.now(),
                poster=poster
            )
        else:
            
            Post.objects.create(
                title=title,
                content=content,
                is_published=is_published,
                published_at=timezone.now()
            )

        return redirect('main:home')

    return render(request, 'main/add_post.html')

def blog_detail_view(request: HttpRequest , blog_id:int):
    blog = Post.objects.get(pk=blog_id)


    return render(request, 'main/blog_detail.html' , {"blog" : blog})
   

def blog_update_view(request: HttpRequest , blog_id:int ) :

    blog = Post.objects.get(pk=blog_id)

    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        if "poster" in request.FILES: blog.poster = request.FILES["poster"]
        blog.save()

        


        return redirect("main:blog_detail_view" , blog_id = blog.id)


    return render(request , "main/blog_update.html" , {"blog":blog})


def blog_delete_view(request: HttpRequest , blog_id:int ) :

    blog = Post.objects.get(pk=blog_id)
    blog.delete()

    return redirect('main:home')