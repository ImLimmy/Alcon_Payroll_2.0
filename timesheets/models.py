from django.db import models
from datetime import datetime
from django.conf import settings
from django.db.models import Sum

from calendars.models import CalendarEvent
from extras.models import Ratings
from forms.leave_models import LeaveRequestForm, HalfDayRequestForm, UnderTimeRequestForm
from forms.call_approval_forms import OverTimeForm


class TimeSheet(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='time_sheets_v2')
    date = models.DateField(null=True, blank=True)
    # time_in = models.TimeField(null=True, blank=True)
    # time_out = models.TimeField(null=True, blank=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Time Sheets'
        unique_together = ('user', 'date')

    def __str__(self):
        return f'{self.user}'

    @property
    def hours_work(self):
        t1 = datetime.strptime(str(self.time_in), '%H:%M:%S')
        t2 = datetime.strptime(str(self.time_out), '%H:%M:%S')
        duration = t2 - t1
        return duration.seconds / 3600

    @property
    def hours_ot(self):
        total_time = 0

        for time in self.ot_forms.all():
            total_time += time.total_hours

        return total_time

    @property
    def regular_pay(self):
        return ((self.user.salary_per_day / self.user.shift.final_hours) * self.hours_work)

    @property
    def ot_pay(self):
        pass
        # return ((self.user.salary_per_day / self.user.shift.final_hours) * self.hours_ot)

class TimeInOut(models.Model):
    date = models.ForeignKey(
        TimeSheet, on_delete=models.CASCADE, related_name='time_in_out')
    time_in = models.TimeField(blank=True, null=True)
    time_out = models.TimeField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Time In/Out'

    def __str__(self):
        return f'{self.date}'

    @property
    def total_hours(self):
        if (self.time_in is None and self.time_out) or (self.time_out is None and self.time_in):
            return 4
        else:
            if self.category == "On-Time":
                t1 = 8.5
            else:
                t_in_hours = self.time_in.hour
                t_in_minutes = self.time_in.minute
                t1 = t_in_hours + (t_in_minutes/60)

        try:
            t2_in_hours = self.time_out.hour
            t2_in_minutes = self.time_out.minute
            t2 = t2_in_hours + (t2_in_minutes/60)
            
        except:
            t2 = 0
        hours = t2 - t1
        hours2 = hours - self.date.user.shift.break_time
        return round(hours2, 2)

    @property
    def with_ot(self):
        OT_Form = OverTimeForm.objects.filter(
                user=self.date.user, status='Approved')
        is_holiday = CalendarEvent.objects.filter(
            this_date=self.date.date).exists()
        ratings = Ratings.objects.get(year=self.date.date.year)
        holiday_rate = ratings.holiday_rate
        ot_rate = ratings.overtime_rate
        pay_per_hour = self.date.user.salary_per_day / self.date.user.shift.final_hours
        if OT_Form.exists():
            if is_holiday == True:
                ot_holiday_pay = (pay_per_hour) * (1 - holiday_rate) 
                return round((ot_holiday_pay), 2)
            else:
                ot_pay = pay_per_hour * ot_rate
                return round((ot_pay), 2)
        return 0
    
    @property
    def with_ut_or_hd(self):
        UT_Form = UnderTimeRequestForm.objects.filter(
                user=self.date.user, status='Approved')
        HD_Form = HalfDayRequestForm.objects.filter(
                user=self.date.user, status='Approved')
        pay_per_hour = self.date.user.salary_per_day / self.date.user.shift.final_hours
        if HD_Form.exists() or UT_Form.exists():
            if self.hours_work <=4:
                half_day = HD_Form.aggregate(
                    Sum(HalfDayRequestForm.total_hours))
                half_day_deduction = (half_day['total_hours__sum'] * pay_per_hour)
                return f'Half Day Deduction: {round((half_day_deduction), 2)}'
            else:
                under_time = UT_Form.aggregate(
                    Sum(UnderTimeRequestForm.total_hours))
                under_time_deduction = (under_time['total_hours__sum'] * pay_per_hour)
                return f'Undertime Deduction: {round((under_time_deduction), 2)}'
        return 0

    @property
    def with_leave_form(self):
        LeaveForm = LeaveRequestForm.objects.filter(
                user=self.date.user, status='Approved')
        pay_per_hour = self.date.user.salary_per_day / self.date.user.shift.final_hours
        is_holiday = CalendarEvent.objects.filter(
            this_date=self.date.date).exists()
        ratings = Ratings.objects.get(year=self.date.date.year)
        holiday_rate = ratings.holiday_rate
        if LeaveForm.exists():
            if is_holiday == True:
                leave_holiday_pay = (pay_per_hour) * (1 - holiday_rate)
                return round((leave_holiday_pay), 2)
            return 0
        return 0
        
    @property
    def payroll_amount(self):
        pay_per_day = self.date.user.salary_per_day
        total_hours = self.date.user.shift.final_hours
        pay_per_hour = pay_per_day / total_hours
        if self.total_hours < total_hours:
            return round((pay_per_hour * self.total_hours), 2)
        else:
            return round((pay_per_day), 2)
        

class OTFormV2(models.Model):
    ts_v2 = models.ForeignKey(
        TimeSheet, on_delete=models.CASCADE, related_name='ot_forms')
    from_time = models.TimeField(("From"))
    to_time = models.TimeField(("To"))
    reason = models.TextField()

    def __str__(self):
        return f'{self.from_time} - {self.to_time}'

    @property
    def total_hours(self):

        # manila_tz = timezone.get_default_timezone()
        # formatted_date = self.date_modified.astimezone(
        #     manila_tz).strftime('%b. %d, %Y, %I:%M %p')

        t1 = datetime.strptime(str(self.from_time), '%H:%M:%S')
        t2 = datetime.strptime(str(self.to_time), '%H:%M:%S')
        duration = t2 - t1
        return duration.seconds / 3600

    

