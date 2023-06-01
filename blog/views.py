from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Post
from .forms import PostForm


def index(request):
    # Variables for displays posts on homepage
    posts = Post.objects.order_by('timestamp')
    context = {'posts': posts}

    # Displays homepage
    return render(request, 'blog/index.html', context)

@login_required
def new_post(request):
    # Creates a new post on the site
    if request.method != "POST":
        # Creates an empty form
        form = PostForm()
    else:
        # If form isn't empty
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('blog:index')

    # Displays an empty or an invalid form
    context = {'form': form}
    return render(request, 'blog/new_post.html', context)

@login_required
def edit_post(request, post_id):
    # Edit the post
    post = Post.objects.get(id=post_id)
    if post.author != request.user:
        raise Http404

    if request.method != 'POST':
        # If form is empty
        form = PostForm(instance=post)
    else:
        # Sends POST-data, saves changes
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')

    context = {'post': post, 'form': form}
    return render(request, 'blog/edit_post.html/', context)

@login_required()
def delete_post(request, post_id):
    # Deletes existing posts
    post = Post.objects.get(id=post_id)
    post.delete()
    # Changes homepage
    return redirect('blog:index')
