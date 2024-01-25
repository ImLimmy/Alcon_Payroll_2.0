from rest_framework import serializers
from .models import TimeSheet, TimeInOut
        
        
class TimeInOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeInOut
        exclude = ['date']
        
        
class TimeSheetSerializer(serializers.ModelSerializer):
    time_in_out = TimeInOutSerializer(many=True)
    
    class Meta:
        model = TimeSheet
        exclude = ['user']

