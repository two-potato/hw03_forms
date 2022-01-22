from django.shortcuts import get_object_or_404, render

# from django.views.generic import (
#     ListView,
#     TemplateView,
#     DetailView,
#     CreateView,
#     UpdateView,
# )

# from django.urls import reverse_lazy
from .models import Group, Post, User
from .forms import PostForm

# from django.contrib import messages
# from django.utils.text import slugify
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    posts_count = posts.count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user': user,
        'posts': posts,
        'posts_count': posts_count,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    # user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(pk=post_id)
    # posts_count = Post.objects.filter(author=get_object_or_404(User, username=username))
    posts_count = posts.count()
    context = {
        'posts': posts,
        'posts_count': posts_count,
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})


# class Index(ListView):
#     model = Post
#     template_name = 'posts/index.html'
#     context_object_name = 'posts'
#     paginate_by = 5

#     def get_context_data(self, *args, **kwargs):
#         posts = Post.objects.all()
#         return {
#             'posts': posts,
#         }


# class GroupPosts(ListView):
#     model = Group
#     template_name = 'posts/group_list.html'
#     paginate_by = 2

#     def get_context_data(self, *args, **kwargs):
#         group = get_object_or_404(Group)
#         posts = group.posts.all()
#         return {
#             'group': group,
#             'posts': posts,
#         }


# class Profile(ListView):
#     model = Post
#     template_name = 'posts/profile.html'

#     def get_queryset(self):
#         return User.objects.all().order_by('-date_joined')


# class PostDetail(DetailView):
#     model = Post
#     template_name = 'posts/post_detail.html'


# class PostCreateView(CreateView):
#     model = Post
#     fields = ('text', 'group')
#     template_name='posts/create_post.html'

#     def success_url(self):
#         messages.success(self.request, 'Great!!! New post created')

#         return reverse_lazy('posts:index')

#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.author = self.request.user
#         obj.slug = slugify(form.cleaned_data['title'])
#         obj.save()
#         return super().form_valid(form)


# class PostUpdateView(UpdateView):
#     model = Post
#     fields = ('author', 'text', 'group')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         update = True
#         context['update'] = update

#         return context

#     def get_success_url(self):
#         messages.success(
#             self.request, 'Your post has been updated successfully.'
#         )
#         return reverse_lazy("posts:index")

#     def get_queryset(self):
#         return self.model.objects.filter(author=self.request.user)
