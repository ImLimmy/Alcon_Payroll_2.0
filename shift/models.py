from django.db import models
from datetime import datetime

# class LaterC(models.Model):
#     if Temp_Shift_Form.exists():
#                 if Temp_Shift_Form.exists():
#                     pass
#                 pass
#             else:
#                 pass # make it Call Approval


class BreakTemplate(models.Model):
    break_start_time = models.TimeField()
    break_end_time = models.TimeField()

    def __str__(self):
        return f'{self.break_start_time} - {self.break_end_time}'

    class Meta:
        abstract = True


class Shift(models.Model):
    shift_name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    grace_period = models.PositiveIntegerField(null=True, blank=True)

    # optional field
    # buffer_time = models.PositiveIntegerField(null=True, blank=True)
    # cross_days = models.PositiviveIntegerField(null=True, blank=True)

    # Work day
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    # On Call day
    monday_on_call = models.BooleanField(default=False)
    tuesday_on_call = models.BooleanField(default=False)
    wednesday_on_call = models.BooleanField(default=False)
    thursday_on_call = models.BooleanField(default=False)
    friday_on_call = models.BooleanField(default=False)
    saturday_on_call = models.BooleanField(default=False)
    sunday_on_call = models.BooleanField(default=False)

    class Meta:
        ordering = ['shift_name']

    def __str__(self) -> str:
        return f'{self.shift_name}'

    @property
    def formatted_start_time(self):
        return self.start_time.strftime("%I:%M %p")

    @property
    def formatted_end_time(self):
        return self.end_time.strftime("%I:%M %p")

    @property
    def schedule(self):
        return f'{self.start_time.strftime("%I:%M %p")} - {self.end_time.strftime("%I:%M %p")}'

    @property
    def shift_breaks(self):
        return [f'{break_obj.break_start_time.strftime("%I:%M %p")} - {break_obj.break_end_time.strftime("%I:%M %p")}' for break_obj in Break.objects.filter(shift=self)]

    @property
    def break_time(self):
        for i in self.breaks.all():
            return i.break_duration

    @property
    def total_hours(self):
        t1 = self.start_time.hour + self.start_time.minute / 60
        t2 = self.end_time.hour + self.end_time.minute / 60
        hours = t2 - t1
        return hours

    @property
    def final_hours(self):
        t1 = self.total_hours
        t2 = self.break_time
        total_time = t1 - t2
        return total_time

    @property
    def days(self):
        days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                        'Thursday', 'Friday', 'Saturday', 'Sunday']
        return [day_of_week for day_of_week, is_true in zip(days_of_week, [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday, self.saturday, self.sunday]) if is_true]

    @property
    def on_call(self):
        on_call_days = ['Monday', 'Tuesday', 'Wednesday',
                        'Thursday', 'Friday', 'Saturday', 'Sunday']
        return [on_call_days for on_call_days, is_true in zip(on_call_days, [self.monday_on_call, self.tuesday_on_call, self.wednesday_on_call, self.thursday_on_call, self.friday_on_call, self.saturday_on_call, self.sunday_on_call]) if is_true]


class Break(BreakTemplate):
    shift = models.ForeignKey(
        Shift, on_delete=models.CASCADE, related_name='breaks')

    @property
    def break_duration(self):
        t1 = self.break_start_time.hour + self.break_start_time.minute / 60
        t2 = self.break_end_time.hour + self.break_end_time.minute / 60
        duration = t2 - t1
        return duration     
