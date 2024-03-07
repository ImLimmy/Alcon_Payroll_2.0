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
        models = Payroll
        fields = '__all__'


class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
<<<<<<< HEAD
        fields = ['id', 'cutoff_name', 'get_start_date', 'get_end_date']
        
class PayrollUserSerializer(serializers.ModelSerializer):
    
    time_in_out = TimeInOutSerializer(many=True)
    
    class Meta:
        model = TimeSheet
        fields = ['id', 'user', 'time_in_out']
        
=======
        fields = '__all__'
>>>>>>> exp_back_end
