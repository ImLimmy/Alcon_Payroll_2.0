from .models import CalendarEvent
from rest_framework import serializers


class EventList_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEvent
        fields = [
            'event',
            'date',
        ]


class EventCreate_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEvent
        fields = '__all__'


class EventDetail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEvent
        fields = '__all__'
