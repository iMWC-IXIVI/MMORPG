from django.urls import path, include
from django.contrib.auth.views import TemplateView

from .views import PostList, PostDetail, PostCreate, PostUpdate, UserPost, UserPostDetail
from response.views import ResponseCreate


urlpatterns = [
    path('post/', PostList.as_view(), name='list_post'),
    path('post/<int:pk>/', PostDetail.as_view(), name='detail_post'),
    path('post/my_posts/<int:pk>/update/', PostUpdate.as_view(), name='update_post'),
    path('post/create/', PostCreate.as_view(), name='add_post'),
    path('post/<int:pk>/response/create/', ResponseCreate.as_view(), name='response_create'),
    path('post/my_posts/', UserPost.as_view(), name='posts_user'),
    path('post/my_posts/<int:pk>/', UserPostDetail.as_view(), name='post_user_detail')
]
