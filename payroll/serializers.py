from rest_framework import serializers

from .models import Payroll
from timesheets.models import TimeSheet
from timesheets.serializers import TimeInOutSerializer


class PayrollListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = ['id', 'cutoff_name', 'get_start_date', 'get_end_date']
        
class PayrollUserSerializer(serializers.ModelSerializer):
    
    time_in_out = TimeInOutSerializer(many=True)
    
    class Meta:
        model = TimeSheet
        fields = ['id', 'user', 'time_in_out']
        