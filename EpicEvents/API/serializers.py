from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from drf_writable_nested import UniqueFieldsMixin
from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from rest_framework import fields
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Client
from .models import Contract
from .models import Event


User = get_user_model()


class UserSignupSerializer(ModelSerializer):

    tokens = SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'phone_number',
            'group',
            'tokens'
        ]

    def validate_email(self, value: str) -> str:
        if User.objects.filter(email=value).exists():
            raise ValidationError('User already exists')
        return value

    def validate_password(self, value: str) -> str:
        if value is not None:
            return make_password(value)
        raise ValidationError('Password is empty')

    def get_tokens(self, user: User) -> dict:
        tokens = RefreshToken.for_user(user)
        data = {
            'refresh': str(tokens),
            'access': str(tokens.access_token)
        }
        return data


class UserSerializer(UniqueFieldsMixin, ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'group',
        ]


class ClientSerializer(UniqueFieldsMixin, ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'mobile',
            'company_name',
            'date_created',
            'date_updated',
            'sales_contact'
        ]


class ContractSerializer(ModelSerializer):
    payment_due = fields.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'])

    class Meta:
        model = Contract
        fields = [
            'id',
            'sales_contact',
            'client',
            'date_created',
            'date_updated',
            'status',
            'payment_amount',
            'payment_due'
        ]


class EventSerializer(UniqueFieldsMixin, ModelSerializer):
    event_date = fields.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'])

    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'support_contact',
            'client',
            'date_created',
            'date_updated',
            'event_status',
            'attendees',
            'event_date',
            'notes'
        ]
        extra_kwargs = {
            'name': {'read_only': False, 'validators': []},
        }
