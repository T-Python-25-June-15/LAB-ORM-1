from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Post


def home_view(request:HttpRequest):

    posts = Post.objects.all()

    return render(request,'main/home.html',{"posts" : posts})

def add_post_view(request:HttpRequest):
   
   if request.method == "POST":
       new_post = Post(title=request.POST["title"], content=request.POST["content"])
       new_post.save()

   return render(request, 'main/add_post.html')
  

