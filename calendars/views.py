from .serializers import *
from .models import CalendarEvent
from rest_framework import generics, permissions

class EventList(generics.ListAPIView):
    queryset = CalendarEvent.objects.all()
    serializer_class = EventList_Serializer
    permission_classes = [permissions.IsAuthenticated]
    
class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CalendarEvent.objects.all()
    serializer_class = EventDetail_Serializer
    permission_classes = [permissions.IsAuthenticated]
    
class EventCreate(generics.CreateAPIView):
    queryset = CalendarEvent.objects.all()
    serializer_class = EventCreate_Serializer
    permission_classes = [permissions.IsAdminUser]