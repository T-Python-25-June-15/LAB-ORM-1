from django.shortcuts import render
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
        post = Post(title=request.POST['title'],content=request.POST['content'],is_published=is_publish)
        post.save()


    return render(request, "add_post.html")