from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Blogger

# Create your views here.
def blogg_view(request : HttpRequest):
    
    if request.method == "POST":
       newBlogg = Blogger(title=request.POST["title"], content=request.POST["content"], 
                         is_published=request.POST["is_published"], published_at=request.POST["published_at"])
       
       newBlogg.save()
    return render(request, "blogger_app/blogger.html")