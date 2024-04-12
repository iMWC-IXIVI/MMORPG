from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Response
from .forms import ResponseCreateForm
from .filters import FilterResponse


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

        return super().form_valid(form)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['post_pk'] = self.kwargs['pk']

        return context


class ResponseList(LoginRequiredMixin, ListView):

    model = Response
    template_name = 'responses_list.html'
    context_object_name = 'responses'
    paginate_by = 15

    def get_queryset(self):

        queryset = super().get_queryset()
        self.filter = FilterResponse(self.request.GET, queryset=Response.objects.filter(post_id__user_id=self.request.user.pk))
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter

        return context


class ResponseDetail(LoginRequiredMixin, DetailView):

    model = Response
    template_name = 'detail_response.html'
    context_object_name = 'response'

    def get_queryset(self):
        return Response.objects.filter(post_id__user_id=self.request.user.pk)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['response_not_active'] = not context['response'].active

        return context


@login_required
def delete_response(request, **kwargs):

    response = Response.objects.get(pk=kwargs['pk'])
    response.delete()
    return redirect('my_response')


@login_required
def activate_response(request, **kwargs):

    response = Response.objects.get(pk=kwargs['pk'])
    response.active = True
    response.save()

    return redirect('my_response')
