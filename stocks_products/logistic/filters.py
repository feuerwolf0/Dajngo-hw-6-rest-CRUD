import django_filters
from django_filters.rest_framework import FilterSet

from .models import Stock


class StockFilter(FilterSet):
    products = django_filters.CharFilter(field_name='positions__product__id')
    quantity = django_filters.CharFilter(field_name='positions__quantity')
    price = django_filters.CharFilter(field_name='positions__price')

    class Meta:
        model = Stock
        fields = ['products', 'quantity', 'price']