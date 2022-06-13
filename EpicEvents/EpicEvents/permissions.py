from rest_framework.permissions import BasePermission
from API.models import Client, Contract, Event


class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.group.name == 'adminmanagement_member':
            print('checked manager true')
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return True


class IsSales(BasePermission):
    message = "You don't have permission to do that. Need to be Sales or Management member"

    def has_permission(self, request, view):
        if request.user and request.user.group.name == 'sales_member':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if type(obj) == Contract or type(obj) == Client or type(obj) == Event:
            if view.action in ['update', 'partial_update', 'retrieve', 'list']:
                return True
            if view.action == 'destroy':
                return False


class IsSupport(BasePermission):
    message = "You don't have permission to do that. Need to be Support or Management member"

    def has_permission(self, request, view):
        if request.user and request.user.group.name == 'support_member':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if type(obj) == Contract or type(obj) == Client:
            if view.action in ['retrieve', 'list']:
                return True
            if view.action in ['update', 'partial_update', 'destroy']:
                return False
        if type(obj) == Event:
            if view.action in ['update', 'partial_update', 'retrieve', 'list']:
                return True
            if view.action == 'destroy':
                return False
