from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Blogger
from datetime import datetime


# Create your views here.
def blogg_view(request : HttpRequest):
    
    if request.method == "POST":
       newBlogg = Blogger(title=request.POST["title"], content=request.POST["content"], 
                         is_published=request.POST["is_published"], 
                         published_at = datetime.fromisoformat(request.POST["published_at"])
                         ,poster=request.FILES["poster"])     
       newBlogg.save()

       return redirect('main:home_view')
    return render(request, "blogger_app/blogger.html")

def blogg_detail_view(request : HttpRequest, blogg_id:int):
    blogg= Blogger.objects.get(pk=blogg_id)
    return render(request, "blogger_app/blogg_detail.html",{"blogg":blogg})

def blogg_update_view(request : HttpRequest, blogg_id:int):
    blogg= Blogger.objects.get(pk=blogg_id)
    if request.method == "POST":
       blogg.title = request.POST["title"]
       blogg.content = request.POST["content"]
       blogg.is_published = request.POST["is_published"]
       blogg.published_at = datetime.fromisoformat(request.POST["published_at"])    
       if "poster" in request.FILES:
           blogg.poster = request.FILES["poster"]

       blogg.save()
       
           
       return redirect('blogger_app:blogg_detail_view',blogg_id)
    return render(request, "blogger_app/blogg_update.html",{"blogg":blogg})

def blogg_delete_view(request : HttpRequest, blogg_id:int):
     blogg= Blogger.objects.get(pk=blogg_id)
     blogg.delete()
     return redirect('main:home_view')