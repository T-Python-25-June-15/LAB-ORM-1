from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from main.models import Post

# Create your views here.


def home_view(request: HttpRequest) -> HttpResponse:
    all_posts = Post.objects.all()
    return render(request, 'main/homepage.html', context={'posts':all_posts})


def create_post_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        post = Post(title=request.POST.get('title') , content=request.POST.get('content') , is_published= bool(request.POST.get('is_published')), published_at= request.POST.get('published_at'))
        post.save()
    return render(request, 'main/new_post.html')