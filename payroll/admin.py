from django.contrib import admin
from .models import Payroll


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['cutoff_name', 'get_period']
=======
    list_display = ['get_period', 'get_gross_pay']
>>>>>>> exp_back_end


# @admin.register(PayrollPerUser)
# class PayrollPerUserAdmin(admin.ModelAdmin):
#     list_display = ['user', 'date']
