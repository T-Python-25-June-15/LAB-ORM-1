from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def home_view(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')#.exclude(content__contains="barcelona")
    return render(request, 'blog/home.html', {'posts': posts})

def add_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})


