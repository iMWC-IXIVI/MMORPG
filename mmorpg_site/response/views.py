from django.shortcuts import render
from django.contrib.auth.views import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import EmailMultiAlternatives

from .models import Response
from post.models import Post
from .forms import ResponseCreateForm


class ResponseCreate(LoginRequiredMixin, CreateView):
    model = Response
    form_class = ResponseCreateForm
    success_url = reverse_lazy('list_post')
    template_name = 'add_response.html'

    def form_valid(self, form):
        data = form.save(commit=False)

        pk = self.kwargs['pk']

        data.post_id = pk
        data.user_id = self.request.user.pk

        data.save()

        post = Post.objects.get(pk=pk)

        html_content = (f'<h1>You have a response at post</h1>'
                        f'<p>Id post: {pk}</p>'
                        f'<p>Title post: {post.title}</p>'
                        f'<p>User response: {self.request.user}</p>')

        message = EmailMultiAlternatives(subject='You have response',
                                         to=[post.user.email])

        message.attach_alternative(html_content, mimetype='text/html')
        message.send()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['post_pk'] = self.kwargs['pk']

        return context
