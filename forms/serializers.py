from rest_framework import serializers

from .leave_models import LeaveRequestForm, HalfDayRequestForm, UnderTimeRequestForm
from .call_approval_forms import CashAdvanceForm, OverTimeForm, TemporaryShiftForm, From_to
from .kpi_models import Kpi

# Cash Advance Form


class CashAdvanceCreateSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CashAdvanceForm
        fields = ['id', 'user', 'date',
                  'cash_amount', 'payment_term', 'description', 'status']


class CashAdvanceListSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CashAdvanceForm
        fields = ['id', 'user', 'date',
                  'cash_amount', 'payment_term', 'status']


class CashAdvanceDetailSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CashAdvanceForm
        fields = ['id', 'user', 'date',
                  'cash_amount', 'payment_term', 'description', 'deduction', 'remaining_amount', 'status']

# Half-Day Form


class HalfDayCreateSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = HalfDayRequestForm
        fields = ['id', 'user', 'start_date',
                  'end_date', 'status', 'description']


class HalfDayListSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = HalfDayRequestForm
        fields = ['id', 'user', 'start_date',
                  'end_date', 'description', 'status']


class HalfDayDetailSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = HalfDayRequestForm
        fields = ['id', 'user', 'start_date',
                  'end_date', 'description', 'half_day', 'total_hours', 'approved_by', 'approved_date', 'status']

# kpi Form


class KpiCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kpi
        exclude = [
            'created_at',
            'updated_at',
        ]


class KpiListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kpi
        fields = [
            'id'
        ]


class KpiDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kpi
        fields = '__all__'

# Leave Form


class LeaveCreateSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = LeaveRequestForm
        fields = ['id', 'user', 'start_date',
                  'end_date', 'description', 'status', 'leave_type']


class LeaveListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = LeaveRequestForm
        exclude = ['description', 'created_at', 'updated_at']


class LeaveDetailSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = LeaveRequestForm
        fields = '__all__'


# Undertime Form

class UnderTimeCreateSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = UnderTimeRequestForm
        fields = ['id', 'user', 'start_date',
                  'end_date', 'description', 'status']


class UnderTimeListSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UnderTimeRequestForm
        fields = ['id', 'user', 'start_date', 'end_date',
                  'description', 'under_time', 'total_hours', 'status']


class UnderTimeDetailSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = UnderTimeRequestForm
        fields = ['id', 'user', 'start_date', 'end_date',
                  'description', 'under_time', 'total_hours', 'approved_by', 'approved_date', 'status']

# Overtime Form


class FromToSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = From_to
        exclude = ['overtime_form']


class OverTimeCreateSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    ot_form = FromToSerializer(many=True)
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    
    class Meta:
        model = OverTimeForm
        fields = ['user', 'date', 'ot_form', 'status', 'created_at', 'updated_at']

    def create(self, validated_data):
        overtime_data = validated_data.pop('ot_form')
        instance_ot = OverTimeForm.objects.create(**validated_data)
        for data in overtime_data:
            From_to.objects.create(overtime_form=instance_ot, **data)
        return instance_ot

    def update(self, instance, validated_data):
        overtime_data = validated_data.pop('ot_form')
        instance = super().update(instance, validated_data)
        existing_data = From_to.objects.filter(overtime_form=instance)
        for obj in existing_data:
            if not any(item.get('id') == obj.id for item in overtime_data):
                obj.delete()
        for data in overtime_data:
            From_to.objects.create(overtime_form=instance, **data)
        return instance


class OverTimeListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OverTimeForm
        exclude = ['created_at', 'updated_at']


class OverTimeDetailSerializer(serializers.ModelSerializer):
    ot_form = FromToSerializer(many=True)
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = OverTimeForm
        fields = ['id', 'user', 'date', 'ot_form', 'status', 'created_at', 'updated_at']

# Temporary Shift Form


class TemporaryShiftCreateSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TemporaryShiftForm
        fields = ['id', 'user', 'start_date',
                  'end_date', 'description', 'status']


class TemporaryShiftListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TemporaryShiftForm
        exclude = ['description', 'created_at', 'updated_at']


class TemporaryShiftDetailSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = TemporaryShiftForm
        fields = ['id', 'user', 'start_date', 'end_date',
                  'description', 'status', 'schedule', 'shift_breaks']
