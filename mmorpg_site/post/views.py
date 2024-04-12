import os
import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import PostCreationForm
from .models import Post
from user.models import Subscribe


class PostList(LoginRequiredMixin, ListView):
    """Вывод списка объявлений"""
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()
    paginate_by = 15

    def get_context_data(self, **kwargs):
        """Контекстная переменная, используемая в шаблонах"""
        context = super().get_context_data(**kwargs)

        context['is_not_subscribe'] = not Subscribe.objects.filter(user_id=self.request.user.pk)

        return context


class PostDetail(LoginRequiredMixin, DetailView):
    """Детальная информация объявления"""
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        """Контекстная переменная, используемая в шаблонах"""
        context = super().get_context_data(**kwargs)
        context['create_response'] = not self.request.user == context['post'].user

        return context


class PostCreate(LoginRequiredMixin, CreateView):
    """Создание объявления"""
    model = Post
    form_class = PostCreationForm
    template_name = 'add_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('list_post')

    def form_valid(self, form):
        """Автоматический ввод пользователя в модель Post"""
        data = form.save(commit=False)
        data.user = self.request.user
        data.save()
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    """Изменение объявления, доступная только пользователям, которые создали объявление"""
    model = Post
    form_class = PostCreationForm
    template_name = 'post_update.html'
    success_url = reverse_lazy('posts_user')

    def get_queryset(self):
        """Вывод данных из базы данных"""
        return Post.objects.filter(user_id=self.request.user.pk)

    def form_valid(self, form):
        """Добавление времени изменения объявления
        Далее реализация удаления файлов в случае, если их в объявлении нет"""
        data = form.save(commit=False)
        data.date_change = datetime.datetime.now()

        post = Post.objects.get(pk=self.kwargs['pk'])

        src_instance = []
        src_instance_data = []

        for instance in post.text.split():
            if 'src=' in instance:
                src_instance.append(instance[6:-1])

        for instance_data in data.text.split():
            if 'src=' in instance_data:
                src_instance_data.append(instance_data[6:-1])

        for image in src_instance:
            if not image in src_instance_data:
                os.remove(f'{image}')

        data.save()

        return super().form_valid(form)


class UserPost(LoginRequiredMixin, ListView):
    """Объявления пользователя"""
    model = Post
    template_name = 'posts_user.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        """Вывод данных из базы данных"""
        return Post.objects.filter(user_id=self.request.user.pk)


class UserPostDetail(LoginRequiredMixin, DetailView):
    """Детальная информация объявления"""
    model = Post
    template_name = 'post_user_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        """Вывод данных из базы данных"""
        return Post.objects.filter(user_id=self.request.user.pk)
