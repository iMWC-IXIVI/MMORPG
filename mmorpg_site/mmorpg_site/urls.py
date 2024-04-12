from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),  # Админ панель
    path('ckeditor5/', include('django_ckeditor_5.urls'), name='ck_editor_5_upload_file'),  # Загрузка файлов CKEditor5
    path('', include('user.urls'), name='user'),  # Пути из приложения user
    path('', include('post.urls'), name='post'),  # Пути из приложения post
    path('', include('response.urls'), name='response')  # Пути из приложения response
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Выгрузка изображений
