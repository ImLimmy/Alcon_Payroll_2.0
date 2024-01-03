from django.contrib import admin

from .models import Incentives, Deductions

@admin.register(Incentives)
class IncentivesAdmin(admin.ModelAdmin):
    list_display = ('incentive_name', 'incentive_amount')
    
@admin.register(Deductions)
class DeductionsAdmin(admin.ModelAdmin):
    list_display = ('deduction_name', 'deduction_amount')