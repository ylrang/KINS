import django_filters
from django_filters import DateFilter
from .models import Docs, Site
from django import forms
from django_filters import DateRangeFilter, DateFilter

COMPANY_CHOICE = (
    ('BRNC', 'BRNC'),
    ('NCSqaure', 'NCSquare'),
    ('UNIST', 'UNIST'),
    ('KINS', 'KINS'),
)

class DocsFilter(django_filters.FilterSet):
    date__month = django_filters.DateFilter(field_name='date', lookup_expr='year')

    class Meta:
        model = Docs

        fields = {
            'title'                      :['icontains'],
            'document__serial_num'       :['icontains'],
            'regist_date'                :['year'],
            'tags__tag_content'          :['icontains'],
            'document__institution'       :['in'],
        }

class SiteFilter(django_filters.FilterSet):

    class Meta:
        model = Site

        fields = {
            'title'         :['icontains'],
            'category'      :['icontains'],
            'group'         :['icontains'],
        }
