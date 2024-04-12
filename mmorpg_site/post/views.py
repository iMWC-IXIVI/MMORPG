import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import PostCreationForm
from .models import Post
from user.models import Subscribe


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_not_subscribe'] = not Subscribe.objects.filter(user_id=self.request.user.pk)

        return context


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_response'] = not self.request.user == context['post'].user

        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'add_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('list_post')

    def form_valid(self, form):
        data = form.save(commit=False)
        data.user = self.request.user
        data.save()
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'post_update.html'
    success_url = reverse_lazy('posts_user')

    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.pk)

    def form_valid(self, form):
        data = form.save(commit=False)
        data.date_change = datetime.datetime.now()
        data.save()

        return super().form_valid(form)


class UserPost(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts_user.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class UserPostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_user_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
