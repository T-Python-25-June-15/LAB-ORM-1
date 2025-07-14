from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from main.models import Post

def main_view(request:HttpRequest):
    all_posts = Post.objects.all()
    return render(request, 'home.html', {
        'posts': all_posts
    })


def add_post(request:HttpRequest):

    if request.POST:
        is_publish = True if request.POST['is_published'] == 'show' else False
        post = Post(title=request.POST['title'],content=request.POST['content'],is_published=is_publish,image = request.FILES['image'])
        post.save()
        return redirect('main:main_view')


    return render(request, "add_post.html")



def post_details_view(request:HttpRequest,id:int):
    post = Post.objects.get(pk=id)
    return render(request,'post_details.html',{
        "post":post
    })


def post_edit_view(request:HttpRequest, id:int):
    post = Post.objects.get(pk=id)

    if request.POST:
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.is_published = True if request.POST['is_published'] == 'show' else False
        post.published_at = request.POST['published_at']
        if post.image in request.FILES:
            post.image = request.FILES['image']
        post.save()
        return redirect('main:main_view')



    return render(request,'edit_post.html',{
        "post":post
    })


def post_delete_view(request:HttpRequest, id:int):
    post = Post.objects.get(pk=id)
    if post:
        post.delete()
        return redirect('main:main_view')
