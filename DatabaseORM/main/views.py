from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from blogs.models import Blogger

def main_page(request:HttpRequest):

  blogs = Blogger.objects.all()

  return render(request, 'main/index.html', {"blogs":blogs})
