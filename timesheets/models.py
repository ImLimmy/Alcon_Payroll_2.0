from django.db import models
from django.utils import timezone
from api.choices import TimeStatus
from users.models import User


class TimeLogs(models.Model):
    file_upload = models.FileField(upload_to='uploads/')
    employee_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    time_log = models.JSONField()

    class Meta:
        verbose_name = 'Time Log'
        verbose_name_plural = 'Time Logs'


class TimeSheet(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='time_sheets')
    date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['date']
        verbose_name_plural = 'Time Sheets'


class TimeInOut(models.Model):
    date = models.ForeignKey(
        TimeSheet, on_delete=models.CASCADE, related_name='time_in_out')
    time_in = models.TimeField(blank=True, null=True)  # first in
    time_out = models.TimeField(blank=True, null=True)  # last out
    

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Time In Out'

    def __str__(self):
        return f'{self.time_in} - {self.time_out}'
