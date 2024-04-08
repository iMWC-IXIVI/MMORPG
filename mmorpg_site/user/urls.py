from django.urls import path, include

from .views import MainView, SignInView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', MainView.as_view(), name='register'),
    path('sign-in/', SignInView.as_view(template_name='sign_in.html'), name='sign_in')
]
