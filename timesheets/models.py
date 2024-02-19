from django.db import models
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.db.models import Sum
from datetime import time as dtime

from calendars.models import CalendarEvent
from extras.models import Ratings
from forms.leave_models import LeaveRequestForm, HalfDayRequestForm, UnderTimeRequestForm
from forms.call_approval_forms import OverTimeForm, From_to, CashAdvanceForm, TemporaryShiftForm
from shift.models import Shift


class TimeSheet(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='time_sheets_v2')
    date = models.DateField(null=True, blank=True)
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Time Sheets'
        unique_together = ('user', 'date')

    def __str__(self):
        return f'{self.date}'

    @property
    def hours_work(self):
        t1 = datetime.strptime(str(self.time_in), '%H:%M:%S')
        t2 = datetime.strptime(str(self.time_out), '%H:%M:%S')
        duration = t2 - t1
        print(duration.seconds / 3600)
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

    @property
    def total_pay(self):
        pay_per_hour = round((self.user.salary_per_day) /
                             (self.user.shift.final_hours), 2)
        ratings = Ratings.objects.get(year=self.date.year)

        total_hours_of_leave = self.user.number_of_leaves()  # hours

        is_holiday = CalendarEvent.objects.filter(
            this_date=self.date).exists()

        if is_holiday == False:
            regular_rate = ratings.regular_rate

            F_Half_day_Form = HalfDayRequestForm.objects.filter(
                half_day_user=self.user, status='Approved')
            F_Leave_Form = LeaveRequestForm.objects.filter(
                leave_user=self.user, status='Approved')
            F_OT_Form = OverTimeForm.objects.filter(
                overtime_user=self.user, status='Approved')
            F_UT_Form = UnderTimeRequestForm.objects.filter(
                under_time_user=self.user, status='Approved')

            if F_OT_Form.exists():
                compute_overtime = F_OT_Form.aggregate(
                    Sum(From_to.total_hours))
                overtime_pay = compute_overtime['overtime_hours__sum'] * \
                    pay_per_hour
                regular_day_and_overtime = (
                    (regular_rate) * self.user.salary_per_day) + overtime_pay
                print(regular_day_and_overtime)

            if F_Leave_Form.exists():
                compute_leave = F_Leave_Form.aggregate(
                    Sum(LeaveRequestForm.total_hours))

                if compute_leave['total_hours__sum'] <= total_hours_of_leave:
                    regular_day_and_leave = ((regular_rate) * self.user.salary_per_day) - (
                        compute_leave['total_hours__sum'] * pay_per_hour)

                    total_hours_of_leave -= compute_leave['total_hours__sum']
                    print(total_hours_of_leave)

                    print(regular_day_and_leave)
                else:
                    regular_day_and_leave = (
                        (regular_rate) * self.user.salary_per_day)
                    print(regular_day_and_leave)

            if F_Half_day_Form.exists() or F_UT_Form.exists():

                if self.hours_work <= 4:
                    half_day = F_Half_day_Form.aggregate(
                        Sum(HalfDayRequestForm.total_hours))
                    regular_day_and_half_day = (
                        (regular_rate) * self.user.salary_per_day) - (half_day['total_hours__sum'] * pay_per_hour)
                    print(regular_day_and_half_day)

                else:
                    under_time = F_UT_Form.aggregate(
                        Sum(UnderTimeRequestForm.total_hours))
                    regular_day_and_undertime = (
                        (regular_rate) * self.user.salary_per_day) - (under_time['total_hours__sum'] * pay_per_hour)
                    print(regular_day_and_undertime)

            else:
                number_work_hours = self.time_out.hour - self.time_in.hour
                regular_day = ((regular_rate) *
                               (number_work_hours * pay_per_hour))
                print(regular_day)

        else:
            holiday_rate = ratings.holiday_rate

            T_Half_day_Form = HalfDayRequestForm.objects.filter(
                half_day_user=self.user, status='Approved')
            T_Leave_Form = LeaveRequestForm.objects.filter(
                leave_user=self.user, status='Approved')
            T_OT_Form = OverTimeForm.objects.filter(
                overtime_user=self.user, status='Approved')
            T_UT_Form = UnderTimeRequestForm.objects.filter(
                under_time_user=self.user, status='Approved')

            if T_OT_Form.exists():
                compute_overtime = T_OT_Form.aggregate(
                    Sum(From_to.total_hours))
                pay_per_hour = round(
                    (self.user.salary_per_day)/(self.user.shift.final_hours), 2)
                overtime_pay = compute_overtime['overtime_hours__sum'] * \
                    pay_per_hour
                holiday_and_overtime = (
                    (holiday_rate) * self.user.salary_per_day) + overtime_pay
                print(holiday_and_overtime)

            if T_Leave_Form.exists():

                # Temporary code before the line, for testing only

                total_hours_of_leave = 40  # hours

                # -------------------------------------------

                compute_leave = T_Leave_Form.aggregate(
                    Sum(LeaveRequestForm.total_hours))
                if compute_leave['total_hours__sum'] <= total_hours_of_leave:
                    holiday_and_leave = ((holiday_rate) * self.user.salary_per_day) - (
                        compute_leave['total_hours__sum'] * pay_per_hour)

                    total_hours_of_leave -= compute_leave['total_hours__sum']
                    print(total_hours_of_leave)

                    print(holiday_and_leave)
                else:
                    holiday_and_leave = (
                        (holiday_rate) * self.user.salary_per_day)
                    print(holiday_and_leave)

            if T_Half_day_Form.exists() or T_UT_Form.exists():

                if self.hours_work <= 4:
                    half_day = T_Half_day_Form.aggregate(
                        Sum(HalfDayRequestForm.total_hours))
                    holiday_and_half_day = (
                        (holiday_rate) * self.user.salary_per_day) - (half_day['total_hours__sum'] * pay_per_hour)
                    print(holiday_and_half_day)

                else:
                    under_time = T_UT_Form.aggregate(
                        Sum(UnderTimeRequestForm.total_hours))
                    holiday_and_undertime = ((holiday_rate) * self.user.salary_per_day) - (
                        under_time['total_hours__sum'] * pay_per_hour)
                    print(holiday_and_undertime)

            else:
                # number_of_work_hours = TimeInOut.total_hours - Shift.final_hours
                total_hours_worked = 0
                for i in self.time_in_out.all():
                    total_hours_worked += i.total_hours

                number_of_work_hours = total_hours_worked
                holiday = ((holiday_rate) *
                           (number_of_work_hours * pay_per_hour))
                print(holiday)


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
            return "Half Day"
        else:
            if self.category == "On-Time":
                t1 = 8.5
            else:
                t_in_hours = self.time_in.hour
                t_in_minutes = self.time_in.minute
                t1 = t_in_hours + (t_in_minutes/60)

        t2_in_hours = self.time_out.hour
        t2_in_minutes = self.time_out.minute
        t2 = t2_in_hours + (t2_in_minutes/60)
        hours = t2 - t1
        hours2 = hours - self.date.user.shift.break_time
        return round(hours2, 2)


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
        print(duration.seconds / 3600)
        return duration.seconds / 3600
