from django.db import models
from django.utils import timezone
from api.choices import LogStatus

from users.models import User


class Attendance(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='attendance_user')
    date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Attendance'

    @property
    def user_in(self):
        return f'{self.time_in.all().first().time_in} {LogStatus.TIME_IN[0][0]}'

    @property
    def user_out(self):
        return f'{self.time_out.all().first().time_out} {LogStatus.TIME_OUT[1][0]}'


class TimeIn(models.Model):
    date = models.ForeignKey(
        Attendance, on_delete=models.CASCADE, related_name='time_in')
    time_in = models.TimeField()


class TimeOut(models.Model):
    date = models.ForeignKey(
        Attendance, on_delete=models.CASCADE, related_name='time_out')
    time_out = models.TimeField()
