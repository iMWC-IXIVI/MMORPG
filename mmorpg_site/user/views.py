import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string


from dotenv import load_dotenv

from .models import CustomUser, EmailAccept

from .constant import RANDOM_STRING


load_dotenv()


class MainView(TemplateView):
    template_name = 'base_site/index.html'

    def post(self, request, **kwargs):

        user = request.POST['nickname']
        email = request.POST['email']
        password_1 = request.POST['password1']
        password_2 = request.POST['password2']

        if password_1 != password_2:
            return HttpResponse('First password not equal second password')

        token = f'{request.POST["csrfmiddlewaretoken"]}+{RANDOM_STRING}'

        EmailAccept.objects.create(token=token, username=user, password=password_1, email=email)

        return render(request, 'information_email.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_auth'] = not self.request.user.is_authenticated

        return context


def accept_mail(request, **kwargs):

    try:
        data = EmailAccept.objects.get(token=kwargs.get('token'))
    except:
        return HttpResponse('Error')

    try:
        CustomUser.objects.create_user(username=data.username, email=data.email, password=data.password)
        data.delete()
    except:
        return HttpResponse('Error')
    return redirect('sign_in')


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
            token = f'{request.POST["csrfmiddlewaretoken"]}+{RANDOM_STRING}'

            EmailAccept.objects.create(token=token, password=password, email=email)

        return render(request, 'information_email.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_auth'] = not self.request.user.is_authenticated

        return context


def accept_in_mail(request, **kwargs):

    try:
        data = EmailAccept.objects.get(token=kwargs.get('token'))
    except:
        return HttpResponse('Error')

    user = authenticate(request, email=data.email, password=data.password)

    login(request, user)

    data.delete()

    return redirect('list_post')


def logout_user(request):
    logout(request)
    return redirect('sign_in')
