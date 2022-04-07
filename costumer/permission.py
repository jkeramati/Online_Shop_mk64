from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from rest_framework import generics, permissions


class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.user == request.user
        return False


class IsSuperUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and permissions.IsAdminUser:
            return True
        return False
