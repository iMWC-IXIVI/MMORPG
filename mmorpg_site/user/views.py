import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from dotenv import load_dotenv

from .models import CustomUser, EmailAccept, Subscribe
from .forms import UserUpdateForm

from .constant import RANDOM_STRING


load_dotenv()  # загрузка переменных окружения


class MainView(TemplateView):
    """Базовое представление страницы, а так же регистрация пользователя"""
    template_name = 'base_site/index.html'

    def post(self, request, **kwargs):
        """Прием данных от пользователя во время регистрации на форуме"""

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
        """Контекстная переменная используемая в шаблоне"""
        context = super().get_context_data(**kwargs)
        context['is_not_auth'] = not self.request.user.is_authenticated

        return context


def accept_mail(request, **kwargs):
    """Подтверждение регистрации пользователя, а значит создание пользователя"""

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
    """Представление для авторизации пользователя"""
    template_name = 'sign_in.html'

    def post(self, request, *args, **kwargs):
        """Прием данных от пользователя. Так же отправка email-письма (см. в этом приложении signals.py)"""

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
        """Контекстная переменная, используемая в шаблоне"""
        context = super().get_context_data(**kwargs)
        context['is_not_auth'] = not self.request.user.is_authenticated

        return context


def accept_in_mail(request, **kwargs):
    """На почту приходит письмо со ссылкой. Ссылка на данную функцию для авторизации пользователя на форуме.
    Письмо приходит по сигналам (см. в этом приложении signals.py)"""

    try:
        data = EmailAccept.objects.get(token=kwargs.get('token'))
    except:
        return HttpResponse('Error')

    user = authenticate(request, email=data.email, password=data.password)

    login(request, user)

    data.delete()

    return redirect('list_post')


@login_required
def logout_user(request):
    """Выход авторизованного пользователя из аккаунта"""
    logout(request)
    return redirect('sign_in')


@login_required
def add_subscribe(request):
    """Подписка авторизованного пользователя. Добавление пользователя, который нажал на кнопку 'подписаться'"""
    Subscribe.objects.create(user_id=request.user.pk)
    return redirect('list_post')


class UserProfile(LoginRequiredMixin, ListView):
    """Вывод профиля авторизованного пользователя"""
    model = CustomUser
    template_name = 'user_profile.html'
    context_object_name = 'user'

    def get_queryset(self):
        """Данные из базы данных. Пользователь, который вошел на аккаунт"""
        return CustomUser.objects.get(pk=self.request.user.pk)


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    """Изменение профиля пользователя"""
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'user_profile_update.html'
    success_url = reverse_lazy('user_profile')
    context_object_name = 'user'

    def get_queryset(self):
        """Данные из базы данных. Пользователь, который вошел на аккаунт"""
        return CustomUser.objects.filter(pk=self.request.user.pk)

    def form_valid(self, form):
        """Удаление фотографии из хранилища в случае замены фотографии"""
        data = form.save(commit=False)

        if data.image != self.request.user.image and self.request.user.image:
            os.remove(f'upload_files/{self.request.user.image}')

        return super().form_valid(form)
