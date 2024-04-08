from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login

from .models import CustomUser


class MainView(TemplateView):
    template_name = 'base_site/index.html'

    def post(self, request, **kwargs):
        if request.method == 'POST':
            user = request.POST['nickname']
            email = request.POST['email']
            password_1 = request.POST['password1']
            password_2 = request.POST['password2']

            if password_1 != password_2:
                return HttpResponse('First password not equal second password')

            CustomUser.objects.create_user(user, email, password_1)

        return redirect('sign_in')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SignInView(TemplateView):
    template_name = 'sign_in.html'

    def post(self, request, *args, **kwargs):

        try:
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            return HttpResponse('You are dont enter the field')

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return redirect('list_post')

        return redirect('sign_in')
