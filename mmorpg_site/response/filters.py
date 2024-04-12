from django_filters import FilterSet, CharFilter

from .models import Response


class FilterResponse(FilterSet):

    post__title = CharFilter(lookup_expr='icontains', label='Post title')

    class Meta:
        model = Response
        fields = ['post__category']
