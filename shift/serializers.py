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

    def create(self, validated_data):
        breaks_data = validated_data.pop('breaks', [])
        shift = Shift.objects.create(**validated_data)
        for break_data in breaks_data:
            Break.objects.create(shift=shift, **break_data)
        return shift


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
