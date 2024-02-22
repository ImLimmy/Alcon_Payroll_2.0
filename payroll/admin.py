from django.contrib import admin
from .models import Payroll


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ['get_period']


# @admin.register(PayrollPerUser)
# class PayrollPerUserAdmin(admin.ModelAdmin):
#     list_display = ['user', 'date']
