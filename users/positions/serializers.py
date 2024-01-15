from .models import Position
from rest_framework import serializers
from users.serializers import UserListSerializer


class Position_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            'position',
        ]


class PositionList_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            'id',
            'position',
        ]


class PositionDetail_Serializer(serializers.ModelSerializer):
    position_users = UserListSerializer(many=True, read_only=True)
    class Meta:
        model = Position
        fields = '__all__'
