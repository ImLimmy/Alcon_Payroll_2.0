from rest_framework import serializers
from .models import TimeLogs, TimeSheet, TimeInOut

class TimeLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLogs
        fields = '__all__'

class TimeSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSheet
        fields = '__all__'

class TimeInOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeInOut
        fields = '__all__'