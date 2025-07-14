from django.shortcuts import render, redirect
from .models import Post

def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        Post.objects.create(title=title, content=content,image=image)
        return redirect('home')
    return render(request, 'blog/add_post.html')


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')

        if request.FILES.get('image'): 
            post.image = request.FILES.get('image')

        post.save()
        return redirect('post_detail', post_id=post.id)

    return render(request, 'blog/edit_post.html', {'post': post})

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'blog/delete_post.html', {'post': post})
