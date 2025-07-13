from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from blooger_app.models import Blogger
# Create your views here.
def home_view(request : HttpRequest):
   bloggers = Blogger.objects.all()
   return render(request, "main/home.html" ,{"bloggers" : bloggers})

def contact_view(request : HttpRequest):
    return render(request, "main/contact.html")


def mode_view(request : HttpRequest, mode):
    response= redirect(request.GET.get("next"),"/")

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")
  
    return response