from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls'), name='ck_editor_5_upload_file'),
    path('', include('user.urls'), name='user'),
    path('', include('post.urls'), name='post'),
    path('', include('response.urls'), name='response')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
