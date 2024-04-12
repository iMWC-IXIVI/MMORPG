from django.urls import path, include

from .views import ResponseList, ResponseDetail, delete_response, activate_response


urlpatterns = [
    path('my_responses/', ResponseList.as_view(), name='my_response'),  # Список откликов
    path('my_responses/<int:pk>/', ResponseDetail.as_view(), name='detail_response'),  # Детальная информация
    path('my_responses/<int:pk>/delete/', delete_response, name='delete_response'),  # Удаление отклика
    path('my_response/<int:pk>/activate/', activate_response, name='activate_response')  # Активация отклика
]
