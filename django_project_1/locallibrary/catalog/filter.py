from django import forms
from catalog.models import Keyword, Book
import django_filters

class KeywordFilter(django_filters.FilterSet):
    words = django_filters.CharFilter(lookup_expr='icontains')
    #year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    #groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Book
        fields = ['keyword_s','title', 'author', 'publisher', 'page', 'position']
