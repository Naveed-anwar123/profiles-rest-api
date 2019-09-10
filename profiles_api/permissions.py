from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow Users to edit thier own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check use is trying to edit thier own profile"""
        #safe methods means it is get method, not put,patch or delete method, means database is safe
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id # Means user is authenticated

