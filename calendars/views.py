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
        ph_holidays = holidays.PH(years=[datetime.now().year])
        existing_events = CalendarEvent.objects.filter(this_date__in=ph_holidays.keys())
        
        new_events_created = []
        for date, name in sorted(ph_holidays.items()):
            if date not in existing_events.values_list('this_date', flat=True):
                new_event = CalendarEvent.objects.create(
                    event=name, this_date=date, is_regular_holiday=True, label="red"
                )
                new_events_created.append(name)

        if new_events_created:
            response_msg = f"Events have been added: {', '.join(new_events_created)}"
        else:
            response_msg = "No new events were added, existing events were already present"

        return Response(response_msg, status=status.HTTP_200_OK)
    

# class PopulateCalendarEvents(APIView):
#     def post(self, request, format=None):
#         ph_holidays = holidays.PH(years=[datetime.now().year])
#         for date, name in sorted(ph_holidays.items()):
#             CalendarEvent.objects.create(
#                 event=name, this_date=date, is_regular_holiday=True, label="red")
#         return Response(f'{'Holidays has been populated'}', status=status.HTTP_200_OK)
