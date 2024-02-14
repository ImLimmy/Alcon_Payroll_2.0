# from django.db import models
# from datetime import datetime
# from django.utils import timezone
# from django.conf import settings
# from django.db.models import Sum

# from calendars.models import CalendarEvent
# from extras.models import Ratings
# from forms.leave_models import LeaveRequestForm, HalfDayRequestForm, UnderTimeRequestForm
# from forms.call_approval_forms import OverTimeForm, From_to, CashAdvanceForm, TemporaryShiftForm



# class TimeSheetV2(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='time_sheets_v2')
#     date = models.DateField()
#     time_in = models.TimeField()
#     time_out = models.TimeField()

#     class Meta:
#         ordering = ['-date']
#         verbose_name_plural = 'Time Sheets'
#         unique_together = ('user', 'date')

#     def __str__(self):
#         return f'{self.date}'

#     @property
#     def hours_work(self):
#         t1 = datetime.strptime(str(self.time_in), '%H:%M:%S')
#         t2 = datetime.strptime(str(self.time_out), '%H:%M:%S')
#         duration = t2 - t1
#         print(duration.seconds / 3600)
#         return duration.seconds / 3600
    
#     @property
#     def hours_ot(self):
#         total_time = 0
        
#         for time in self.ot_forms.all():
#             total_time += time.total_hours
        
#         return total_time
    
#     @property  
#     def regular_pay(self):
#         return ((self.user.salary_per_day / self.user.shift.final_hours) * self.hours_work)

#     @property
#     def ot_pay(self):
#         pass
#         # return ((self.user.salary_per_day / self.user.shift.final_hours) * self.hours_ot) 
    
#     @property
#     def total_pay(self):
#         ratings = Ratings.objects.get(year=self.date.year)
#         is_holiday = CalendarEvent.objects.filter(
#             this_date=self.date).exists()            

#         if is_holiday == False:
#             regular_rate = ratings.regular_rate
            
#             F_Half_day_Form = HalfDayRequestForm.objects.filter(
#                 half_day_user=self.user, status='Approved')
#             F_Leave_Form = LeaveRequestForm.objects.filter(
#                 leave_user=self.user, status='Approved')
#             F_OT_Form = OverTimeForm.objects.filter(
#                 overtime_user= self.user, status='Approved')
#             F_UT_Form = UnderTimeRequestForm.objects.filter(
#                 under_time_user=self.user, status='Approved')
#             F_Temp_Shift_Form = TemporaryShiftForm.objects.filter(
#                 temp_shift_user=self.user, status='Approved')
            
#             if F_OT_Form.exists():
#                 compute_overtime = F_OT_Form.aggregate(Sum(From_to.total_hours))
#                 pay_per_hour = round((self.user.salary_per_day)/(self.user.shift.final_hours), 2)
#                 overtime_pay = compute_overtime['overtime_hours__sum'] * pay_per_hour
#                 regular_day_and_overtime = ((regular_rate) * self.user.salary_per_day) + overtime_pay
#                 print(regular_day_and_overtime)
#             if F_Leave_Form.exists():
#                 compute_leave = F_Leave_Form.aggregate(Sum(From_to.total_hours))
#                 pass
            
#             else:
#                 pay_per_hour = round((self.user.salary_per_day)/(self.user.shift.final_hours), 2)
#                 regular_pay = ((regular_rate) * self.user.salary_per_day)
#                 print(regular_pay)
                
#         else:
#             holiday_rate = ratings.holiday_rate
            
#             T_Half_day_Form = HalfDayRequestForm.objects.filter(
#                 half_day_user=self.user, status='Approved')
#             T_Leave_Form = LeaveRequestForm.objects.filter(
#                 leave_user=self.user, status='Approved')
#             T_OT_Form = OverTimeForm.objects.filter(
#                 overtime_user=self.user, status='Approved')
#             T_Temp_Shift_Form = TemporaryShiftForm.objects.filter(
#                 temp_shift_user=self.user, status='Approved')
            
#             if T_OT_Form.exists():
#                 compute_overtime = T_OT_Form.aggregate(Sum(From_to.total_hours))
#                 pay_per_hour = round((self.user.salary_per_day)/(self.user.shift.final_hours), 2)
#                 overtime_pay = compute_overtime['overtime_hours__sum'] * pay_per_hour
#                 holiday_and_overtime = ((holiday_rate) * self.user.salary_per_day) + overtime_pay
#                 print(holiday_and_overtime)
                
#             if T_Temp_Shift_Form.exists():
#                 pass
            
#             else:
#                 pass
            
#             # return self.regular_pay + (self.ot_pay * 1.25)
            
            
# class OTFormV2(models.Model):
#     ts_v2 = models.ForeignKey(
#         TimeSheetV2, on_delete=models.CASCADE, related_name='ot_forms')
#     from_time = models.TimeField(("From"))
#     to_time = models.TimeField(("To"))
#     reason = models.TextField()

#     def __str__(self):
#         return f'{self.from_time} - {self.to_time}'

#     @property
#     def total_hours(self):

#         # manila_tz = timezone.get_default_timezone()
#         # formatted_date = self.date_modified.astimezone(
#         #     manila_tz).strftime('%b. %d, %Y, %I:%M %p')

#         t1 = datetime.strptime(str(self.from_time), '%H:%M:%S')
#         t2 = datetime.strptime(str(self.to_time), '%H:%M:%S')
#         duration = t2 - t1
#         print(duration.seconds / 3600)
#         return duration.seconds / 3600
