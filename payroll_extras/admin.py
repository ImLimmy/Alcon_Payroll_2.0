from django.contrib import admin

from .models import Incentives, Deductions, Ratings

@admin.register(Incentives)
class IncentivesAdmin(admin.ModelAdmin):
    list_display = ('incentive_name', 'incentive_amount')
    
@admin.register(Deductions)
class DeductionsAdmin(admin.ModelAdmin):
    list_display = ('deduction_name', 'deduction_amount')

@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ('year', 
                    'ordinary_days', 
                    'sunday_or_rest_days',
                    'special_nonworking_days',
                    'special_nonworking_and_rest_days',
                    'double_special_nonworking_days',
                    'double_special_nonworking_and_rest_days',
                    'regular_holidays',
                    'regular_holiday_and_rest_days',
                    'double_holidays',
                    'double_holidays_and_rest_days',
                    'night_shifts',
                    'night_shift_and_special_nonworking_days',
                    'night_shift_special_nonworking_and_rest_days',
                    'night_shift_and_double_special_nonworking_days',
                    'night_shift_and_regular_holidays',
                    'night_shift_regular_holiday_and_rest_days',
                    'night_shift_and_double_holidays',
                    'night_shift_double_holidays_and_rest_days',
                    'ordinary_and_overtime_days',
                    'rest_day_and_overtime_days',
                    'special_nonworking_day_and_overtime_days',
                    'special_nonworking_rest_day_and_overtime_days',
                    'double_special_nonworking_rest_day_and_overtime_days',
                    'regular_holiday_and_overtime_days',
                    'rest_day_night_shift_and_overtime_days',
                    'special_nonworking_day_rest_day_night_shift_and_overtime_days',
                    'double_special_nonworking_rest_days_night_shift_and_overtime_days',
                    'regular_holiday_rest_day_night_shift_and_overtime_days',
                    'night_shift_and_double_holidays_and_overtime_days',
                    'night_shift_double_holidays_rest_days_and_overtime_days',
                    )
    