from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post  
from django.utils import timezone



def home_view(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.filter(is_published=True).order_by('-published_at')


    return render(request, "main/home_view.html", {"posts": posts})




def post_delete_view(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":

        
        post.delete()


        return redirect("main:home_view")
    

    return render(request, "main/confirm_delete.html", {"post": post})





def post_update_view(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        if "image" in request.FILES:
            post.image = request.FILES["image"]
        post.save()
        return redirect("main:post_detail_view", post_id=post.id)
    return render(request, "main/post_update.html", {"post": post})






def post_detail_view(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "main/post_detail.html", {"post": post})






def add_post_view(request: HttpRequest) -> HttpResponse:


    if request.method == "POST":

        
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
        )



        new_post.save()



        return redirect("home_view")
    

    return render(request, "main/add_post_view.html")



def mode_view(request:HttpRequest, mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")


    return response





