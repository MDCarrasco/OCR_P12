from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from API.models import User, Client, Contract, Event
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', )


class UserAdmin(BaseUserAdmin):
    @property
    def filter_horizontal(self):
        return ()

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_filter = ('group', )
    exclude = ('username',)
    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'email', 'password')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'group')}),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'group')}
        ),
    )
    list_display = ('id', 'email', )
    ordering = ('email',)


admin.site.register(User, UserAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_filter = ('email', 'last_name', 'date_created')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'sales_contact':
            kwargs["queryset"] = User.objects.filter(group__name='sales_member')
        return super(ClientAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Client, ClientAdmin)


class ContractAdmin(admin.ModelAdmin):
    list_filter = ('date_created',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'sales_contact':
            kwargs["queryset"] = User.objects.filter(group__name='sales_member')
        return super(ContractAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Contract, ContractAdmin)


class EventAdmin(admin.ModelAdmin):
    list_filter = ('event_status', 'date_created')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'support_contact':
            kwargs["queryset"] = User.objects.filter(group__name='support_member')
        return super(EventAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Event, EventAdmin)
