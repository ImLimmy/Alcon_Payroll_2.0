from .serializers import (
    EventList_Serializer,
    EventDetail_Serializer,
    EventCreate_Serializer,
    )
from .models import CalendarEvent
from api.mixins import UserPermissionMixin, AdminPermissionMixin
from rest_framework import generics, permissions

class EventList(UserPermissionMixin, generics.ListAPIView):
    queryset = CalendarEvent.objects.all()
    serializer_class = EventList_Serializer
    
class EventDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = CalendarEvent.objects.all()
    serializer_class = EventDetail_Serializer
    
class EventCreate(AdminPermissionMixin, generics.CreateAPIView):
    queryset = CalendarEvent.objects.all()
    serializer_class = EventCreate_Serializer