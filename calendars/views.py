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
    
    def get_serializer_class(self):
        
        if self.request.method == 'PUT' and self.request.user.is_staff:
            return EventCreate_Serializer
        return super().get_serializer_class()


class EventCreate(AdminPermissionMixin, generics.CreateAPIView):
    queryset = CalendarEvent.objects.all()
    serializer_class = EventCreate_Serializer
