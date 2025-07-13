from django.shortcuts import render
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
      
    new_blog = Blogger(title=request.POST["title"], content=request.POST["content"], is_published = status)
    new_blog.save()


  return render(request, 'main/add.html')
