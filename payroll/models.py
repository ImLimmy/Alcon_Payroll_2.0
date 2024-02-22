from django.db import models
from timesheets.models import TimeSheet
# Create your models here.

class Payroll(models.Model):
    # cutoff_name = models.CharField(max_length=255)
    get_start_date = models.DateField()
    get_end_date = models.DateField()

    def __str__(self):
        return f'date ranges from {self.get_start_date} to {self.get_end_date}'

    @property
    def get_period(self):
        queryset = TimeSheet.objects.filter(date__range=[self.get_start_date, self.get_end_date])
        print(queryset.values())

#     @property
#     def get_user_id(self):
#         return self.user.employee_id

#     @property
#     def get_full_name(self):
#         return self.user.full_name()

#     @property
#     def get_basic_pay(self):
#         return 

#     @property
#     def get_gross_pay():
#         pass

#     @property
#     def get_deduction():
#         pass

#     @property
#     def get_net_pay():
#         pass


# class PayrollPerUser(models.Model):
#     payroll = models.ForeignKey(
#         Payroll, on_delete=models.SET_NULL, null=True, related_name='payroll_records')

#     # pay_per_day =

#     pass
