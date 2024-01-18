from .models import Shift, Break
from rest_framework import serializers


class BreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Break
        exclude = ['shift']


class ShiftCreateSerializer(serializers.ModelSerializer):
    breaks = BreakSerializer(many=True)

    class Meta:
        model = Shift
        fields = '__all__'


class ShiftListSerializer(serializers.ModelSerializer):
    breaks = BreakSerializer(many=True)

    class Meta:
        model = Shift
        fields = ['id', 'shift_name', 'schedule', 'breaks', 'days', 'on_call']


class ShiftDetailSerializer(serializers.ModelSerializer):
    breaks = BreakSerializer(many=True)

    class Meta:
        model = Shift
        fields = '__all__'
