from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Post


def home_view(request:HttpRequest):

    posts = Post.objects.all()
    return render(request,'main/home.html',{"posts" : posts})

def add_post_view(request:HttpRequest):
   
   if request.method == "POST":
       new_post = Post(title=request.POST["title"], content=request.POST["content"], poster=request.FILES["poster"])
       new_post.save()

       return redirect('main:home_view')
   return render(request, 'main/add_post.html')



def post_detail_view(request:HttpRequest, post_id:int):

    post=Post.objects.get(pk=post_id)

    return render(request,'main/post_detail.html',{'post': post})


def post_update_view(request:HttpRequest,post_id:int):
    post=Post.objects.get(pk=post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content=request.POST["content"]
        if "poster" in request.FILES: post.poster = request.FILES["poster"]
        post.save()

      
        return redirect('main:post_update_view',post_id=post.id)


    return render(request,'main/post_update.html',{'post': post})


def post_delete_view(request:HttpRequest,post_id:int):

    post=Post.objects.get(pk=post_id)
    post.delete

    return redirect("main:home_view")