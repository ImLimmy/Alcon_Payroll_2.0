from rest_framework import serializers

from .models import Incentives, Deductions, Ratings


class IncentivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incentives
        fields = '__all__'


class IncentivesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incentives
        fields = [
            'id',
            'incentive_name',
            'incentive_amount',
        ]


class IncentivesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incentives
        fields = '__all__'


class DeductionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deductions
        fields = '__all__'


class DeductionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deductions
        fields = [
            'id',
            'deduction_name',
            'deduction_amount',
        ]


class DeductionsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deductions
        fields = '__all__'


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'


class RatingsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = [
            'id',
            'year',
        ]


class RatingsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'
