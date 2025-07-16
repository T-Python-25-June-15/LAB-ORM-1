from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from posts.models import Post

# Create your views here.

def home_view(request):
    latest_posts = Post.objects.filter(is_published=True).order_by("-published_at")
    return render(request, 'main/home.html', {"posts": latest_posts})
    