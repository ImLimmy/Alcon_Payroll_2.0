from .serializers import AttendanceSerializer, TimeInSerializer, TimeOutSerializer
from .models import Attendance, TimeIn, TimeOut
from rest_framework import generics, permissions

class AttendanceList(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

class TimeInList(generics.ListCreateAPIView):
    queryset = TimeIn.objects.all()
    serializer_class = TimeInSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
class TimeInDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeIn.objects.all()
    serializer_class = TimeInSerializer
    permission_classes = [permissions.IsAuthenticated]

class TimeOutList(generics.ListCreateAPIView):
    queryset = TimeOut.objects.all()
    serializer_class = TimeOutSerializer
    permission_classes = [permissions.IsAuthenticated]

class TimeOutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeOut.objects.all()
    serializer_class = TimeOutSerializer
    permission_classes = [permissions.IsAuthenticated]