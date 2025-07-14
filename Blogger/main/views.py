from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.utils import timezone


# Create your views here.

def home_view(request:HttpRequest):
    
    # get all posts
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts':posts})


def add_view (request:HttpRequest):

    if request.method == 'POST':
        if request.method == 'POST':
            title = request.POST["title"]
            content = request.POST["content"]
            published_at = request.POST["published_at"] or timezone.now()
            image = request.FILES.get("image")  # returns None if not uploaded

            if image: # if the user upload an image
                new_post = Post(
                    title=title,
                    content=content,
                    published_at=published_at,
                    image=image
                )
            else: # display the default image
                new_post = Post(
                    title=title,
                    content=content,
                    published_at=published_at
                 )

            new_post.save()
            return redirect('main:home_view')

    return render(request, 'add.html', {"now":timezone.now()})

def detail_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)

    return render(request, "details.html", {"post":post})


def update_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.published_at = request.POST['published_at']

        if "image" in request.FILES: post.image = request.FILES["image"]
        post.save()

        return redirect("main:detail_view", post_id = post.id)


    return render(request, "update.html", {"post":post})

def delete_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect("main:home_view")


