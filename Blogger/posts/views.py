from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
 


def home(request):
    posts = Post.objects.all().order_by('-published_at')
    return render(request, 'posts/home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('home') 
