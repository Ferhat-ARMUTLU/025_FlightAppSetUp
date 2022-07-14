from cmath import e
from rest_framework import permissions

class ItStafforReadOnly(permissions.IsAdminUser):

     def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
        #    return bool(request.user and request.user.is_staff)
             return bool( request.user.is_staff)