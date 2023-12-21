from .serializers import (
    AttendanceSerializer, 
    TimeInSerializer, 
    TimeOutSerializer,
    )
from .models import (
    Attendance, 
    TimeIn, 
    TimeOut,
    )
from api.mixins import UserPermissionMixin
from rest_framework import generics, permissions

class AttendanceList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class TimeInList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = TimeIn.objects.all()
    serializer_class = TimeInSerializer
    
class TimeInDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeIn.objects.all()
    serializer_class = TimeInSerializer

class TimeOutList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = TimeOut.objects.all()
    serializer_class = TimeOutSerializer

class TimeOutDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeOut.objects.all()
    serializer_class = TimeOutSerializer