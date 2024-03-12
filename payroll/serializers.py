from rest_framework import serializers

from .models import Payroll
from timesheets.models import TimeSheet
from timesheets.serializers import TimeInOutSerializer


class PayrollListSerializer(serializers.ModelSerializer):
    get_basic_pay = serializers.StringRelatedField(read_only=True)
    get_gross_pay = serializers.StringRelatedField(read_only=True)
    get_deduction = serializers.StringRelatedField(read_only=True)
    get_ot_amount = serializers.StringRelatedField(read_only=True)  
    get_net_pay = serializers.StringRelatedField(read_only=True)
    time_in_out  = TimeInOutSerializer(read_only=True, required = False)
    class Meta:
        model = Payroll
        fields = '__all__'


class PayrollDetailSerializer(serializers.ModelSerializer):
    get_basic_pay = serializers.StringRelatedField(read_only=True)
    get_gross_pay = serializers.StringRelatedField(read_only=True)
    get_deduction = serializers.StringRelatedField(read_only=True)
    get_ot_amount = serializers.StringRelatedField(read_only=True)  
    get_net_pay = serializers.StringRelatedField(read_only=True)
    time_in_out  = TimeInOutSerializer(read_only=True, required = False)

    class Meta:
        model = Payroll
        fields = '__all__'


class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = '__all__'
