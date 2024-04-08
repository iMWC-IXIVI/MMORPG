from django.urls import path, include
from django.contrib.auth.views import TemplateView


urlpatterns = [
    path('post/', TemplateView.as_view(template_name='posts.html'), name='list_post')
]