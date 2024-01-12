from .models import Careers
from rest_framework import serializers


class CareersCreate_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = '__all__'


class CareersList_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = [
            'id',
            'career_status',
            'career_description',
        ]


class CareersDetail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = '__all__'
