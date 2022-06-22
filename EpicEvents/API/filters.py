from django_filters import rest_framework as filters
from .models import Contract, Client, Event


class ContractFilter(filters.FilterSet):
    date_created = filters.CharFilter(field_name='date_created', lookup_expr='icontains')
    payment_amount = filters.NumberFilter(field_name='payment_amount', lookup_expr='gte')
    client_last_name = filters.CharFilter(field_name='client__last_name', lookup_expr='icontains')
    client_email = filters.CharFilter(field_name='client__email', lookup_expr='iexact')

    class Meta:
        model = Contract
        fields = ['date_created', 'payment_amount', 'client', ]


class ClientFilter(filters.FilterSet):
    last_name = filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    email = filters.CharFilter(field_name='email', lookup_expr='iexact')

    class Meta:
        model = Client
        fields = ['last_name', 'email', ]


class EventFilter(filters.FilterSet):
    event_name = filters.CharFilter(field_name='name', lookup_expr='iexact')
    event_date = filters.CharFilter(field_name='event_date', lookup_expr='icontains')
    client_last_name = filters.CharFilter(field_name='client__last_name', lookup_expr='icontains')
    client_email = filters.CharFilter(field_name='client__email', lookup_expr='iexact')

    class Meta:
        model = Event
        fields = ['name', 'event_date', 'client', ]
