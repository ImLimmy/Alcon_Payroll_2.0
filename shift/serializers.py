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
        fields = ['id', 'shift_name', 'start_time', 'end_time', 'breaks', 'days', 'on_call']


class ShiftDetailSerializer(serializers.ModelSerializer):
    breaks = BreakSerializer(many=True, read_only=True)
    
    def update(self, instance, validated_data):
        breaks_data = validated_data.pop('breaks', [])
        for break_data in breaks_data:
            # Update individual break instances
            break_instance = instance.breaks.get(id=break_data.get('id'))
            break_instance.start_time = break_data.get('break_start_time')
            break_instance.end_time = break_data.get('break_end_time')
            break_instance.save()
        return super().update(instance, validated_data)

    class Meta:
        model = Shift
        fields = '__all__'
