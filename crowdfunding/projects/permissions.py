from rest_framework import permissions

#Checks if user is owner or if request is GET method
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): #determines whether or not user has access to a model instance
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user #returns T/F, checks if the requestor is the project owner