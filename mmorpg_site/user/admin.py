from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from django.utils.safestring import mark_safe

from .forms import AdminUserCreationForm, AdminUserChangeForm
from .models import CustomUser


class AdminUserModel(UserAdmin):
    form = AdminUserChangeForm
    add_form = AdminUserCreationForm
    list_display = ['email', 'username', 'date_creation', 'get_image']
    search_fields = ['username', 'email']
    ordering = ['date_creation']
    list_filter = ['username', 'email']
    filter_horizontal = []
    readonly_fields = ['get_image']
    fieldsets = [
        ('Main information', {'fields': ['username', 'get_image', 'image']}),
        ('Personal info', {'fields': ['email', 'password']}),
        ('Permissions', {'fields': ['is_staff', 'is_superuser']})
    ]
    add_fieldsets = [(None, {'classes': ['wide'],
                             'fields': ['email', 'username', 'password']})]

    def get_image(self, instance):
        if instance.image:
            return mark_safe(f'<img src={instance.image.url} width="250", height="100"')
        return ''

    get_image.short_description = 'My image'


admin.site.register(CustomUser, AdminUserModel)

admin.site.unregister(Group)
