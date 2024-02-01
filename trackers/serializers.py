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
            'leave_user',
            'leave_type',
            'start_date',
            'end_date',
            'status',
            'approved_by',
            'approved_date',
        ]


class LeaveTrackerDetail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveTracker
        fields = '__all__'
