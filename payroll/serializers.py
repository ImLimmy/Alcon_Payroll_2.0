from rest_framework import serializers

from .models import Payroll
from timesheets.models import TimeSheet
from timesheets.serializers import TimeInOutSerializer


# class PayrollListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Payroll
#         fields = '__all__'


class PayrollDetailSerializer(serializers.ModelSerializer):

    get_gross_pay = serializers.StringRelatedField(read_only=True)
    get_deduction = serializers.StringRelatedField(read_only=True)
    get_net_pay = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Payroll
        fields = '__all__'


class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = '__all__'
