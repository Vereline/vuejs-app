from django_graphene_permissions.permissions import BasePermission
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission to only allow admins of an object to edit it.
    Assumes the model instance has an `is_staff` attribute.
    """

    def has_object_permission(self, request, view, obj):
        """
        Called when .get_object() is called (edit object)
        """
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `is_staff`.
        return bool(request.user and request.user.is_staff)

    def has_permission(self, request, view):
        """
        Called when object is created
        """
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `is_staff`.
        return bool(request.user and request.user.is_staff)


class BlogPostSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 7


class IsAdminOrReadOnlyGraphQL(BasePermission):

    @staticmethod
    def has_permission(context):
        return context.user and context.user.is_authenticated

    @staticmethod
    def has_object_permission(context, obj):
        return True


class IsAuthenticatedGraphQL(BasePermission):

    @staticmethod
    def has_permission(context):
        return context.user and context.user.is_authenticated

    @staticmethod
    def has_object_permission(context, obj):
        return True
