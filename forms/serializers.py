from rest_framework import serializers

from .cash_advance_models import CashAdvanceForm
from .half_day_models import HalfDayForm
from .leave_models import LeaveForm
from .overtime_models import OverTimeForm
from .kpi_models import Kpi
from .tempshift_models import TemporaryShiftForm

# Cash Advance Form


class CashAdvanceCreateSerializer(serializers.ModelSerializer):

    cash_advance_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CashAdvanceForm
        fields = ['id', 'cash_advance_user', 'date',
                  'cash_amount', 'term', 'description', 'status']


class CashAdvanceListSerializer(serializers.ModelSerializer):

    cash_advance_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CashAdvanceForm
        exclude = ['created_at', 'updated_at']


class CashAdvanceDetailSerializer(serializers.ModelSerializer):

    cash_advance_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CashAdvanceForm
        fields = '__all__'

# Half-Day Form


class HalfDayCreateSerializer(serializers.ModelSerializer):

    half_day_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = HalfDayForm
        fields = ['id', 'half_day_user', 'date',
                  'time_out', 'description', 'status']


class HalfDayListSerializer(serializers.ModelSerializer):

    half_day_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = HalfDayForm
        exclude = ['time_out', 'description', 'created_at', 'updated_at']


class HalfDayDetailSerializer(serializers.ModelSerializer):

    half_day_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = HalfDayForm
        fields = '__all__'

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
            'kpi_user',
        ]


class KpiDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kpi
        fields = '__all__'

# Leave Form


class LeaveCreateSerializer(serializers.ModelSerializer):

    leave_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = LeaveForm
        fields = ['id', 'leave_user', 'start_date',
                  'end_date', 'description', 'status', 'leave_type']


class LeaveListSerializer(serializers.ModelSerializer):

    leave_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = LeaveForm
        exclude = ['description', 'created_at', 'updated_at']


class LeaveDetailSerializer(serializers.ModelSerializer):

    leave_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = LeaveForm
        fields = '__all__'

# Overtime Form


class OverTimeCreateSerializer(serializers.ModelSerializer):

    overtime_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OverTimeForm
        fields = ['id', 'overtime_user', 'date',
                  'overtime_hours', 'description', 'status']


class OverTimeListSerializer(serializers.ModelSerializer):

    overtime_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OverTimeForm
        exclude = ['overtime_hours', 'description', 'created_at', 'updated_at']


class OverTimeDetailSerializer(serializers.ModelSerializer):

    overtime_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OverTimeForm
        fields = '__all__'

# Temporary Shift Form


class TemporaryShiftCreateSerializer(serializers.ModelSerializer):

    tempshift_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TemporaryShiftForm
        fields = ['id', 'tempshift_user', 'start_date', 'end_date',
                  'start_time', 'end_time', 'description', 'status']


class TemporaryShiftListSerializer(serializers.ModelSerializer):

    tempshift_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TemporaryShiftForm
        exclude = ['description', 'created_at', 'updated_at']


class TemporaryShiftDetailSerializer(serializers.ModelSerializer):

    tempshift_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TemporaryShiftForm
        fields = '__all__'
