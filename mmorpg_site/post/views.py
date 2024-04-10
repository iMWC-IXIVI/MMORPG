import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import PostCreationForm
from .models import Post


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
    success_url = reverse_lazy('list_post')

    def form_valid(self, form):
        data = form.save(commit=False)
        data.date_change = datetime.datetime.now()
        data.save()

        return super().form_valid(form)
