# from django.db import models
# from timesheets.models import TimeSheet, TimeInOut
# from api.choices import Cutoffs

# # Create your models here.


# class Payroll(models.Model):
#     cutoff_name = models.CharField(
#         max_length=255, choices=Cutoffs, default=Cutoffs.FIRST_CUTOFF)
#     start_date = models.DateField()
#     end_date = models.DateField()

#     def __str__(self):
#         return f'{self.cutoff_name}'

#     @property
#     def period(self):
#         return f'{self.start_date} - {self.end_date}'

# #     @property
# #     def get_user_id(self):
# #         return self.user.employee_id

# #     @property
# #     def get_full_name(self):
# #         return self.user.full_name()

# #     @property
# #     def get_basic_pay(self):
# #         return

#     @property
#     def gross_pay(self):
#         basic_amount = TimeInOut.objects.filter(date__range=[self.start_date, self.end_date]).values(
#             'payroll_amount').aggregate(models.Sum('payroll_amount'))['payroll_amount__sum']
#         # ot_amount = TimeInOut.objects.filter(date__range=[self.start_date, self.end_date]).values(
#         #     'with_ot').aggregate(models.Sum('with_ot'))['with_ot__sum']

#         # per_cutoff = basic_amount + ot_amount

#         # return round((per_cutoff), 2)

#     # @property
#     # def get_deduction(self):
#     #     ot_deduction = (TimeInOut.with_ut_or_hd)
#     #     leave_deduction = (TimeInOut.with_leave_form)
#     #     total_deduction = (ot_deduction + leave_deduction)
#     #     return round((total_deduction), 2)

#     # @property
#     # def get_net_pay(self):
#     #     net_pay = self.get_gross_pay - self.get_deduction
#     #     return round((net_pay), 2)


# # class PayrollPerUser(models.Model):
# #     payroll = models.ForeignKey(
# #         Payroll, on_delete=models.SET_NULL, null=True, related_name='payroll_records')

# #     # pay_per_day =

# #     pass
