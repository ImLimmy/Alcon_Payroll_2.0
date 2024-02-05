from .models import Shift, Break
from rest_framework import serializers


class BreakSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Break
        # exclude = ['shift']
        fields = '__all__'


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
        fields = ['id', 'shift_name', 'start_time',
                  'end_time', 'breaks', 'days', 'on_call']


class ShiftDetailSerializer(serializers.ModelSerializer):
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

    def update(self, instance, validated_data):
        breaks_data = validated_data.pop('breaks', [])
        instance = super().update(instance, validated_data)

        existing_data = Break.objects.filter(shift=instance)

        for break_obj in existing_data:
            if not any(item.get('id') == break_obj.id for item in breaks_data):
                break_obj.delete()

        for break_data in breaks_data:
            Break.objects.update_or_create(
                shift=instance, id=break_data.get('id'), defaults={**break_data})

        return instance
