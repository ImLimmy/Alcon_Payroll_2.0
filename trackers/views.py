from rest_framework import generics
from api.mixins import AdminPermissionMixin
from .models import LeaveTracker
from .serializers import (
    LeaveTrackerList_Serializer,
    LeaveTrackerDetail_Serializer
)

class LeaveTrackerList(AdminPermissionMixin, generics.ListCreateAPIView):
    queryset = LeaveTracker.objects.all()
    serializer_class = LeaveTrackerList_Serializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return LeaveTrackerDetail_Serializer
        return super().get_serializer_class()
    
class LeaveTrackerDetail(AdminPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveTracker.objects.all()
    serializer_class = LeaveTrackerDetail_Serializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return LeaveTrackerDetail_Serializer
        return super().get_serializer_class()
