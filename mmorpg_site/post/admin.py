from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as PostAdmin

from .models import Post
from .forms import AdminPostCreationForm, AdminPostChangeForm


class AdminPostModel(PostAdmin):
    add_form_template = 'admin_add/add_form.html'
    fieldsets = (
        (None, {'fields': ('title', 'text', 'category')}),
        ('Personal info', {'fields': ('user', )})
    )
    add_fieldsets = [(None, {'classes': ['wide'],
                             'fields': ['title', 'text', 'category', 'user']})]
    add_form = AdminPostCreationForm
    form = AdminPostChangeForm
    list_display = ('user', 'title')
    list_filter = ('title', )
    search_fields = ('title', )
    ordering = ('date_creation', )
    filter_horizontal = []


admin.site.register(Post, AdminPostModel)
