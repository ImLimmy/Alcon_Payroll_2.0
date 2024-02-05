from .serializers import (
    EventList_Serializer,
    EventDetail_Serializer,
    EventCreate_Serializer,
)
from .models import CalendarEvent
from api.mixins import UserPermissionMixin, AdminPermissionMixin
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
import holidays


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


class PopulateCalendarEvents(APIView):
    def post(self, request, format=None):
        # CalendarEvent.populate_calendar_events()
        ph_holidays = holidays.PH(years=[datetime.now().year])
        for date, name in sorted(ph_holidays.items()):
            CalendarEvent.objects.create(
                event=name, unformat_date=date, is_regular_holiday=True, label="red")
        return Response(f'{'Holidays has been populated'}', status=status.HTTP_200_OK)
