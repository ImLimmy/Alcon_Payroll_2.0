from .models import TimeIn, TimeOut, Attendance
from rest_framework import serializers

class TimeInSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeIn
        fields = '__all__'
        
class TimeOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeOut
        fields = '__all__'
        
class AttendanceSerializer(serializers.ModelSerializer):
    time_in = TimeInSerializer(many=True, read_only=True)
    time_out = TimeOutSerializer(many=True, read_only=True)
    class Meta:
        model = Attendance
        fields = '__all__'