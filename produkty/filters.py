import django_filters
from .models import Product, ProductCategory
from django import forms
from multiselectfield import MultiSelectField

class ProductsFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = {
            'jmeno': ['icontains']
        }

class Filter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category', lookup_expr='icontains')


    class Meta:
        model = ProductCategory
        fields = ['category']
