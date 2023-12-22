from rest_framework import serializers

from .models import (
    PagIbig,
    PhilHealth,
    SSS,
)

class PagIbigSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagIbig
        fields = '__all__'
        
class PhilHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhilHealth
        fields = '__all__'
        
class SSSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSS
        fields = '__all__'