from django.urls import path, include

from .views import ResponseList, ResponseDetail, delete_response, activate_response


urlpatterns = [
    path('my_responses/', ResponseList.as_view(), name='my_response'),
    path('my_responses/<int:pk>/', ResponseDetail.as_view(), name='detail_response'),
    path('my_responses/<int:pk>/delete/', delete_response, name='delete_response'),
    path('my_response/<int:pk>/activate/', activate_response, name='activate_response')
]
