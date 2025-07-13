from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from blog.models import Post
# Create your views here.


def base_view(request):
    
    
    return render(request, "main/base.html", )

def home_view(request):

    cookie_value = request.COOKIES.get('background', "white")
    blogs = Post.objects.all()

    response = render(request, "main/home.html", {"background": cookie_value , "blogs" : blogs})
    return response


def dark_mode(request: HttpRequest, mode: str):
    if mode not in ['light', 'dark']:
        mode = 'light'
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('mode', mode, max_age=60*60*24*30)
    return response    