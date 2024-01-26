from rest_framework import serializers
from .models import TimeSheet, TimeInOut


class TimeSheetListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.get_id_and_username')
    class Meta:
        model = TimeSheet
        fields = '__all__'


class TimeInOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeInOut
        exclude = ['date']


class TimeSheetSerializer(serializers.ModelSerializer):
    time_in_out = TimeInOutSerializer(many=True)

    class Meta:
        model = TimeSheet
        exclude = ['user']
