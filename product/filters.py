import django_filters
from .models import Checkout

class CheckoutFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Checkout
        fields = ['email']