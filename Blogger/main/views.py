from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from main.models import Post

# Create your views here.


def home_view(request: HttpRequest) -> HttpResponse:
    all_posts = Post.objects.all()
    return render(request, 'main/homepage.html', context={'posts':all_posts})


def create_post_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        post = Post(title=request.POST.get('title') , content=request.POST.get('content') , is_published= bool(request.POST.get('is_published')), published_at= request.POST.get('published_at'), poster=request.FILES.get('poster'))
        post.save()
    return render(request, 'main/new_post.html')


def show_details_view(request: HttpRequest, id_post: int) -> HttpResponse:
    post = Post.objects.get(pk=id_post)
    return render(request, 'main/details.html', context={'post': post})


def update_post_view(request: HttpRequest, id_post):
    if request.method == 'POST':
        post = Post.objects.get(pk=id_post)
        post.title = request.POST.get('title')
        post.content=request.POST.get('content')
        post.is_published= bool(request.POST.get('is_published'))
        post.published_at= request.POST.get('published_at')
        post.poster=request.FILES.get('poster')

        if request.FILES.get('poster'): post.poster = request.FILES.get('poster')
        post.save()
        return redirect('main:home_view')
    return render(request, 'main/new_post.html')