from rest_framework import serializers

from .leave_models import LeaveRequestForm, HalfDayRequestForm, UnderTimeRequestForm
from .call_approval_forms import CashAdvanceForm, OverTimeForm, TemporaryShiftForm, From_to
from .kpi_models import Kpi

# Cash Advance Form


class CashAdvanceCreateSerializer(serializers.ModelSerializer):

    cash_advance_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CashAdvanceForm
        fields = ['id', 'cash_advance_user', 'date',
                  'cash_amount', 'payment_term', 'description']


class CashAdvanceListSerializer(serializers.ModelSerializer):

    cash_advance_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CashAdvanceForm
        fields = ['id', 'cash_advance_user', 'date',
                  'cash_amount', 'payment_term']


class CashAdvanceDetailSerializer(serializers.ModelSerializer):

    cash_advance_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CashAdvanceForm
        fields = ['id', 'cash_advance_user', 'date',
                  'cash_amount', 'payment_term', 'description', 'deduction', 'remaining_amount', 'status']

# Half-Day Form


class HalfDayCreateSerializer(serializers.ModelSerializer):

    half_day_user = serializers.StringRelatedField()

    class Meta:
        model = HalfDayRequestForm
        fields = ['id', 'half_day_user', 'start_date',
                  'end_date', 'description']


class HalfDayListSerializer(serializers.ModelSerializer):

    half_day_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = HalfDayRequestForm
        fields = ['id', 'half_day_user', 'start_date',
                  'end_date', 'description', 'status']


class HalfDayDetailSerializer(serializers.ModelSerializer):

    half_day_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = HalfDayRequestForm
        fields = ['id', 'half_day_user', 'start_date',
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
            'id',
        ]


class KpiDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kpi
        fields = '__all__'

# Leave Form


class LeaveCreateSerializer(serializers.ModelSerializer):

    leave_user = serializers.StringRelatedField()

    class Meta:
        model = LeaveRequestForm
        fields = ['id', 'leave_user', 'start_date',
                  'end_date', 'description', 'status', 'leave_type']


class LeaveListSerializer(serializers.ModelSerializer):

    leave_user = serializers.StringRelatedField()

    class Meta:
        model = LeaveRequestForm
        exclude = ['description', 'created_at', 'updated_at']


class LeaveDetailSerializer(serializers.ModelSerializer):

    leave_user = serializers.StringRelatedField()

    class Meta:
        model = LeaveRequestForm
        fields = '__all__'


# Undertime Form

class UnderTimeCreateSerializer(serializers.ModelSerializer):

    under_time_user = serializers.StringRelatedField()

    class Meta:
        model = UnderTimeRequestForm
        fields = ['id', 'under_time_user', 'start_date',
                  'end_date', 'description', 'status']


class UnderTimeListSerializer(serializers.ModelSerializer):

    under_time_user = serializers.StringRelatedField()

    class Meta:
        model = UnderTimeRequestForm
        fields = ['id', 'under_time_user', 'start_date', 'end_date',
                  'description', 'under_time', 'total_hours']


class UnderTimeDetailSerializer(serializers.ModelSerializer):

    under_time_user = serializers.StringRelatedField()

    class Meta:
        model = UnderTimeRequestForm
        fields = ['id', 'under_time_user', 'start_date', 'end_date',
                  'description', 'under_time', 'total_hours', 'approved_by', 'approved_date', 'status']

# Overtime Form


class OTForm(serializers.ModelSerializer):
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = OverTimeForm
        exclude = ['overtime_user', 'created_at', 'updated_at']


class OverTimeCreateSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(read_only=True)
    overtime_users = OTForm(many=True)

    class Meta:
        model = From_to
        fields = ['id', 'overtime_users', 'date', 'from_time', 'to_time',
                  'total_hours', 'description']


class OverTimeListSerializer(serializers.ModelSerializer):

    overtime_user = serializers.StringRelatedField()

    class Meta:
        model = OverTimeForm
        exclude = ['created_at', 'updated_at']


class OverTimeDetailSerializer(serializers.ModelSerializer):
    from_time = OTForm(many=True)
    to_time = OTForm(many=True)
    overtime_user = serializers.StringRelatedField()
    date = serializers.ReadOnlyField(source='ot_form.date.date')
    total_hours = OverTimeCreateSerializer(many=True)
    description = OverTimeCreateSerializer(many=True)

    class Meta:
        model = OverTimeForm
        fields = ['id', 'overtime_user', 'date', 'from_time',
                  'to_time', 'total_hours', 'description']

# Temporary Shift Form


class TemporaryShiftCreateSerializer(serializers.ModelSerializer):

    tempshift_user = serializers.StringRelatedField()

    class Meta:
        model = TemporaryShiftForm
        fields = ['id', 'tempshift_user', 'start_date',
                  'end_date', 'description', 'status']


class TemporaryShiftListSerializer(serializers.ModelSerializer):

    tempshift_user = serializers.StringRelatedField()

    class Meta:
        model = TemporaryShiftForm
        exclude = ['description', 'created_at', 'updated_at']


class TemporaryShiftDetailSerializer(serializers.ModelSerializer):

    tempshift_user = serializers.StringRelatedField()

    class Meta:
        model = TemporaryShiftForm
        fields = ['id', 'tempshift_user', 'start_date', 'end_date',
                  'description', 'status', 'schedule', 'shift_breaks']
