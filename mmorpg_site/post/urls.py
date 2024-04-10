from django.urls import path, include
from django.contrib.auth.views import TemplateView

from .views import PostList, PostDetail, PostCreate, PostUpdate


urlpatterns = [
    path('post/', PostList.as_view(), name='list_post'),
    path('post/<int:pk>/', PostDetail.as_view(), name='detail_post'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='update_post'),
    path('post/create/', PostCreate.as_view(), name='add_post')
]
