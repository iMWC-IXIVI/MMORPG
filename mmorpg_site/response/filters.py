from django_filters import FilterSet, CharFilter

from .models import Response


class FilterResponse(FilterSet):
    """Внутри откликов поиск информации. Фильтрация данных"""
    post__title = CharFilter(lookup_expr='icontains', label='Post title')

    class Meta:
        model = Response
        fields = ['post__category']
