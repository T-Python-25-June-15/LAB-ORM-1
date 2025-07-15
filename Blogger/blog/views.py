from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.utils import timezone



def home_view(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, "blog/index.html", context={"posts" : posts})



def add_post(request: HttpRequest):
    if request.method == "POST":
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
            is_published=True,
            poster=request.FILES["poster"]
        )
        new_post.save()
        return redirect("blog:home_view")
    
    return render(request, "blog/addPost.html")



def post_details_view (request: HttpRequest, post_id: int ):
    post = Post.objects.get(pk=post_id)
    return render(request, "blog/post_details.html", context={"post" : post})


def post_update_view (request: HttpRequest, post_id: int):

    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        if "poster" in request.FILES: 
            post.poster = request.FILES["poster"]
        post.published_at = timezone.now()

        post.save()
        return redirect("blog:post_details_view", post_id=post.id)
        

    return render(request, "blog/post_update.html", context={"post" : post} )




def post_delete_view (request: HttpRequest, post_id: int):

    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect ("blog:home_view")

