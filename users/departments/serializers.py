from .models import Department
from rest_framework import serializers


class Department_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'department',
        ]


class DepartmentList_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentDetail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
