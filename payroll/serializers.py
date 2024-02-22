from rest_framework import serializers

from .models import Payroll


class PayrollListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = '__all__'