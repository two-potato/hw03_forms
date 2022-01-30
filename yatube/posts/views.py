from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post, User


def index(request):
    '''Main page view.'''
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "posts": posts,
        "page_obj": page_obj,
    }
    return render(request, "posts/index.html", context)


def group_posts(request, slug):
    '''Group list view.'''
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    title = f'Страница сообщества {group.title}'

    context = {
        "group": group,
        "page_obj": page_obj,
        'title': title,
    }
    return render(request, "posts/group_list.html", context)


def profile(request, username):
    '''Author profile view.'''
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()
    posts_count = posts.count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "author": user,
        "posts": posts,
        "posts_count": posts_count,
        'page_obj': page_obj,
    }
    return render(request, "posts/profile.html", context)


def post_detail(request, post_id):
    '''Post detail view.'''

    posts = get_object_or_404(Post, id=post_id)
    posts_count = Post.objects.filter(author=posts.author).count()
    user = posts.author
    context = {
        "posts": posts,
        "posts_count": posts_count,
        "user": user,
    }
    return render(request, "posts/post_detail.html", context)


@login_required
def post_create(request):
    '''Post create view.'''
    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("posts:profile", post.author)
    else:
        form = PostForm()

    return render(request, "posts/create_post.html", {"form": form})


@login_required
def post_edit(request, post_id):
    '''Post edit view.'''
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post.id)
    return render(
        request,
        'posts/create_post.html',
        {'form': form, 'is_edit': True, 'post_id': post.id},
    )
