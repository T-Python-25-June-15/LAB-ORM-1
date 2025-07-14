from django.shortcuts import render, redirect
from .models import Post
# Create your views here.


def home_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'main/index.html',  context)


def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = request.POST.get('is_published') == 'on'
        image = request.FILES['image']
        Post.objects.create(
            title=title,
            content=content,
            is_published=is_published,
            image = image
        )
        return redirect('/')

    return render(request, 'main/add_post.html')

def detail_view(request, post_id):
    
    post = Post.objects.get(pk = post_id)
    
    return render(request, 'main/detail.html', {'post':post})


def delete_post(request, post_id):
    
    post = Post.objects.get(pk = post_id)
    
    post.delete()
    return redirect('/')


def update_post(request, post_id):
    
    post = Post.objects.get(pk = post_id)
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_published = request.POST.get('is_published') == 'on'
        if 'image' in request.FILES: post.image = request.FILES['image']
        
        post.save()
        return redirect('/')

    return render(request, 'main/update.html', {'post': post})