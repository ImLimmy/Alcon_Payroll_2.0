from .models import Department
from rest_framework import serializers
from users.serializers import UserListSerializer


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
    department_users = UserListSerializer(many=True, read_only=True)
    class Meta:
        model = Department
        fields = '__all__'
