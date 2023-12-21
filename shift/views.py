from .serializers import (
    ShiftListSerializer,
    ShiftDetailSerializer,
    ShiftCreateSerializer,
)
from .models import Shift
from api.mixins import UserPermissionMixin, AdminPermissionMixin

from rest_framework import generics, permissions

class ShiftList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftListSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST' and self.request.user.is_staff:
            return ShiftCreateSerializer
        return super().get_serializer_class()
        
class ShiftDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftDetailSerializer