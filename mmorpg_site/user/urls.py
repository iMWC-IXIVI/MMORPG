from django.urls import path, include

from django.views.generic import TemplateView

from .views import MainView, SignInView, accept_mail, accept_in_mail


urlpatterns = [
    path('', MainView.as_view(), name='register'),
    path('sign-in/', SignInView.as_view(template_name='sign_in.html'), name='sign_in'),
    path('accept/<str:token>/', accept_mail, name='accept_mail'),
    path('accept-in/<str:token>/', accept_in_mail, name='accept_in_mail')
]
