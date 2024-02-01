from .models import LeaveCounter, LeaveTracker
from rest_framework import serializers


class LeaveCounterlist_Serializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveCounter
        fields = '__all__'


class LeaveCounterDetail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveCounter
        fields = '__all__'


class LeaveTrackerList_Serializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveTracker
        fields = [
            'id',
            'user',
            'date_of_leave',
            'to_date',
            'approved_by',
            'approved_date',
        ]


class LeaveTrackerDetail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveTracker
        fields = '__all__'
