from .models import Shift, Break
from rest_framework import serializers


class BreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Break
        exclude = ['shift']
        # fields = '__all__'


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
        # fields = ['id', 'shift_name', 'formatted_start_time', 'formatted_end_time', 'breaks', 'days', 'on_call']
        fields = ['id', 'shift_name', 'start_time', 'end_time', 'breaks', 'days', 'on_call']

class ShiftDetailSerializer(serializers.ModelSerializer):
    breaks = BreakSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        breaks_data = validated_data.pop('breaks', [])
        instance = super().update(instance, validated_data)
        for break_data in breaks_data:
            if break_data.get('id'):
                break_obj = Break.objects.get(id=break_data.get('id'))
                break_obj.shift = instance
                break_obj.save()
            else:
                Break.objects.create(shift=instance, **break_data)
        return instance

    class Meta:
        model = Shift
        fields = '__all__'
