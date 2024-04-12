from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as ResponseAdmin

from .models import Response
from .forms import AdminResponseChangedForm, AdminResponseCreationForm


class AdminResponseModel(ResponseAdmin):
    """Определение админ панели для откликов"""
    add_form_template = 'admin_add/add_form.html'
    fieldsets = [
        [None, {'fields': ['response']}],
        ['Personal info', {'fields': ['user', 'post']}]
    ]
    add_fieldsets = [[None, {'classes': ['wide'],
                             'fields': ['response', 'user', 'post']}]]
    form = AdminResponseCreationForm
    add_form = AdminResponseChangedForm
    change_password_form = None
    list_display = ['text', 'user', 'post']
    list_filter = ['text', 'user']
    search_fields = ['user']
    ordering = ['date_creation']
    filter_horizontal = []


admin.site.register(Response, AdminResponseModel)  # Регистрация модели Response в админ панели
