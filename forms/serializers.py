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
                  'cash_amount', 'payment_term', 'description', 'status']


class CashAdvanceListSerializer(serializers.ModelSerializer):

    cash_advance_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CashAdvanceForm
        fields = ['id', 'cash_advance_user', 'date',
                  'cash_amount', 'payment_term', 'status']


class CashAdvanceDetailSerializer(serializers.ModelSerializer):

    cash_advance_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CashAdvanceForm
        fields = ['id', 'cash_advance_user', 'date',
                  'cash_amount', 'payment_term', 'description', 'deduction', 'remaining_amount', 'status']

# Half-Day Form


class HalfDayCreateSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = HalfDayRequestForm
        fields = ['id', 'user', 'start_date',
                  'end_date', 'description']


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

class OverTimeCreateSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = From_to
        fields = ['id', 'date', 'from_time', 'to_time',
                  'total_hours', 'description']


class OTForm(serializers.ModelSerializer):
    date = serializers.DateTimeField(read_only=True)
    ot_forms = OverTimeCreateSerializer(many=True)

    class Meta:
        model = OverTimeForm
        exclude = ['user', 'created_at', 'updated_at']


class OverTimeListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)  
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OverTimeForm
        exclude = ['created_at', 'updated_at']


class OverTimeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OverTimeForm
        fields = '__all__'

# Temporary Shift Form


class TemporaryShiftCreateSerializer(serializers.ModelSerializer):

    tempshift_user = serializers.StringRelatedField()

    class Meta:
        model = TemporaryShiftForm
        fields = ['id', 'tempshift_user', 'start_date',
                  'end_date', 'description', 'status']


class TemporaryShiftListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    tempshift_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TemporaryShiftForm
        exclude = ['description', 'created_at', 'updated_at']


class TemporaryShiftDetailSerializer(serializers.ModelSerializer):

    tempshift_user = serializers.StringRelatedField()

    class Meta:
        model = TemporaryShiftForm
        fields = ['id', 'tempshift_user', 'start_date', 'end_date',
                  'description', 'status', 'schedule', 'shift_breaks']
