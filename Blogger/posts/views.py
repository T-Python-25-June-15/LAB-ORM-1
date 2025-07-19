from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
 


def home(request):
    posts = Post.objects.filter( media__gt=1, is_published=True).order_by('-published_at')
    return render(request, 'posts/home.html', {'posts': posts})

def add_post(request):
    try:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
    except Exception as e:
        print(f"Error adding post: {e}")
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})


def delete_post(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return redirect('home')
    except Exception as e:
        print(f"Error deleting post: {e}")
        return redirect('home')


def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            form.save()
            return redirect('details_post', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/update_post.html', {'form': form, 'post': post})


def details_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if not post.is_published:
        return redirect('home') 

    return render(request, 'posts/deatils_post.html', {'post': post})