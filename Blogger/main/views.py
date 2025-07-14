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