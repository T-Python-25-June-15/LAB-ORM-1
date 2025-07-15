from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponse

from .models import Blogger



  # title = models.CharField(max_length=2048)
  # content = models.TextField()
  # is_published = models.BooleanField(default=True)
  # published_at = models.DateField(default=timezone.now)


def add_blog(request:HttpRequest):

  if request.method == "POST":
    status = True

    if request.POST["is_published"] == "0":
      status = False
      
    new_blog = Blogger(
      title=request.POST["title"],
      content=request.POST["content"],
      is_published = status,
      poster=request.FILES["poster"])
    new_blog.save()


  return render(request, 'main/add.html')


def blog_detail_view(request:HttpRequest, blog_id:int):

  blog = Blogger.objects.get(pk=blog_id)

  return render(request, "main/blog_detail.html", {"bloge":blog})

def blog_update_view(request:HttpRequest, blog_id:int):

  blog = Blogger.objects.get(pk=blog_id)
  
  if request.method == "POST":
    status = True

    if request.POST["is_published"] == "0":
      status = False
      
    blog.title=request.POST["title"]
    blog.content=request.POST["content"]
    blog.is_published = status
    blog.poster=request.FILES["poster"]
    blog.save()

  

  return render(request, "main/update.html", {"bloge":blog})

def blog_delete_view(request:HttpRequest, blog_id:int):

  blog = Blogger.objects.get(pk=blog_id)
  blog.delete()

  # return render(request, "")
  return redirect('/')