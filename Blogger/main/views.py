from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from blogs.models import Blog
# Create your views here.


def home_view(request: HttpRequest):
    blogs= Blog.objects.all().order_by('-published_at')


    return render(request, 'main/index.html',{"blogs" : blogs} )


def mode_view(request:HttpRequest, mode):
    response = redirect(request.GET.get("next", "/"))

    if mode== "light":
        response.set_cookie("mode", "light", max_age=-3600)
    elif mode == "dark":
        response.set_cookie("mode", "dark", max_age=60*68*24)
    
    return response