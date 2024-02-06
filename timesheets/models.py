from django.db import models
from django.utils import timezone
from datetime import datetime
from users.models import User
from datetime import time as dtime


class TimeSheet(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='time_sheets')
    date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['date']
        verbose_name_plural = 'Time Sheets'
        unique_together = ('user', 'date')

    def __str__(self):
        return f'{self.date}'


class TimeInOut(models.Model):
    date = models.ForeignKey(
        TimeSheet, on_delete=models.CASCADE, related_name='time_in_out')
    time_in = models.TimeField(blank=True, null=True)  # first in
    time_out = models.TimeField(blank=True, null=True)  # last out
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Time In Out'

    def __str__(self):
        return f'{self.date}'

    @property
    def total_hours(self):
        if (self.time_in is None and self.time_out) or (self.time_out is None and self.time_in):
            return "Half day"
        else:
            if self.category == "On-Time":
                t1 = datetime.strptime(str(dtime(8, 30)), '%H:%M:%S')
            else:
                t1 = datetime.strptime(str(self.time_in), '%H:%M:%S')

            t2 = datetime.strptime(str(self.time_out), '%H:%M:%S')

        hours = t2 - t1
        return hours