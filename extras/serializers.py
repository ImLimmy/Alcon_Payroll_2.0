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
        fields = [
            'id',
            'year',
            'regular_rate', 
            'holiday_rate', 
            'rest_day', 
            'night_rate', 
            'overtime_rate',
            'ordinary_days',
            'ordinary_and_overtime_days',
            'sunday_or_rest_days',
            'rest_day_and_overtime_days',
            'rest_day_night_shift_and_overtime_days',
            'special_nonworking_days',
            'special_nonworking_and_rest_days',
            'special_nonworking_day_and_overtime_days',
            'special_nonworking_rest_day_and_overtime_days',
            'special_nonworking_day_rest_day_night_shift_and_overtime_days',
            'double_holidays',
            'double_holidays_and_rest_days',
            'double_special_nonworking_days',
            'double_special_nonworking_and_rest_days',
            'double_special_nonworking_rest_day_and_overtime_days',
            'double_special_nonworking_rest_days_night_shift_and_overtime_days',
            'regular_holidays',
            'regular_holiday_and_rest_days',
            'regular_holiday_and_overtime_days',
            'regular_holiday_rest_day_night_shift_and_overtime_days',
            'night_shifts',
            'night_shift_and_special_nonworking_days',
            'night_shift_special_nonworking_and_rest_days',
            # 'night_shift_and_double_special_nonworking_days',
            'night_shift_and_regular_holidays',
            'night_shift_regular_holiday_and_rest_days',
            'night_shift_and_double_holidays',
            'night_shift_double_holidays_and_rest_days',
            'night_shift_and_double_holidays_and_overtime_days',
            'night_shift_double_holidays_rest_days_and_overtime_days',
        ]
