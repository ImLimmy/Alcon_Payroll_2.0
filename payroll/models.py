from django.db import models
from timesheets.models import TimeSheet, TimeInOut
# Create your models here.


class Payroll(models.Model):
    # cutoff_name = models.CharField(max_length=255)
    get_start_date = models.DateField()
    get_end_date = models.DateField()

    def __str__(self):
        return f'date ranges from {self.get_start_date} to {self.get_end_date}'

    @property
    def get_period(self):
        queryset = TimeSheet.objects.filter(
            date__range=[self.get_start_date, self.get_end_date])
        # print(queryset.values())

#     @property
#     def get_user_id(self):
#         return self.user.employee_id

#     @property
#     def get_full_name(self):
#         return self.user.full_name()

#     @property
#     def get_basic_pay(self):
#         return

    @property
    def get_gross_pay(self):
        basic_amount = (TimeInOut.payroll_amount)
        ot_amount = (TimeInOut.with_ot)
        
        print(basic_amount)
        if ot_amount == 0:
            return basic_amount

        return 'wassap'
    
    
    # @property
    # def get_deduction(self):
    #     ot_deduction = (TimeInOut.with_ut_or_hd)
    #     leave_deduction = (TimeInOut.with_leave_form)
    #     total_deduction = (ot_deduction + leave_deduction)
    #     return round((total_deduction), 2)

    # @property
    # def get_net_pay(self):
    #     net_pay = self.get_gross_pay - self.get_deduction
    #     return round((net_pay), 2)


# class PayrollPerUser(models.Model):
#     payroll = models.ForeignKey(
#         Payroll, on_delete=models.SET_NULL, null=True, related_name='payroll_records')

#     # pay_per_day =

#     pass
