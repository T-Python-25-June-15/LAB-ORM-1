from django.shortcuts import render
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
        published_at = request.POST.get("published_at") or timezone.now() # get the datetime from the user if exist, otherwise make it now 
        new_post = Post(title = request.POST["title"],content = request.POST["content"], published_at = published_at )
        new_post.save()

    return render(request, 'add.html', {"now":timezone.now()})