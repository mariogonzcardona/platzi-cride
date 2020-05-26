"""Circle views."""

# Django REST Framework
from rest_framework import viewsets,mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import MethodNotAllowed

# Permissions
from rest_framework.permissions import IsAuthenticated
from cride.circles.permissions.circles import IsCircleAdmin

# Serializers
from cride.circles.serializers.circles import CircleModelSerializer

# Models
from cride.circles.models import Circle,Membership

class CircleViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """Circle view set."""
    queryset=Circle.objects.all()
    serializer_class=CircleModelSerializer
    lookup_field='slug_name'
    
    def get_permissions(self):
        """Assign permissions based on action"""
        permissions=[IsAuthenticated]
        if self.action in ["update","partial_update"]:
            permissions.append(IsCircleAdmin)
        return [p() for p in permissions]

    def get_queryset(self):
        """Restrict list to public-only"""
        queryset=Circle.objects.all()
        if self.action=='list':
            return queryset.filter(is_public=True)
        return queryset

    def perform_create(self, serializer):
        """Assign circle admin"""
        circle=serializer.save()
        user=self.request.user
        profile=user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitations=10
        )
        
    def destroy(self,request,pk=None):
        raise MethodNotAllowed('DELETE')
