from django.db import models
from django.utils import timezone
from datetime import time

from api.choices import TimeStatus
from users.models import User


class TimeLogs(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='time_log_user')
    date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Time Logs'


class TimeInput(models.Model):
    time_input = models.TimeField()
    date = models.ForeignKey(
        TimeLogs, on_delete=models.CASCADE, related_name='time_in')

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Time Input'

    @property
    def time_in(self):
        flexi_counter = 3

        if self.time_input <= time(8, 30):
            return f'Log:{TimeStatus.TIME_IN[1][0]} Time: {self.time_input}'
        
        if self.time_input > time(8, 30) and self.time_input <= time(9, 00):
            return f'Log:{TimeStatus.LATE[1][0]} Time: {self.time_input}'
        
        if self.time_input > time(9, 00) and self.time_input <= time(10, 30):
            if flexi_counter != 0:
                flexi_counter -= 1
            return f'Log:{TimeStatus.FLEXI[1][0]} Time: {self.time_input}'
        
        if self.time_input > time(10,30) and self.time_input <= time(12, 00):
            if flexi_counter != 0:
                flexi_counter -= 1
            return f'Log:{TimeStatus.FLEXI[1][0]} and {TimeStatus.LATE} Time: {self.time_input}' 

# class Attendance(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='attendance_user')
#     date = models.DateField(default=timezone.now)

#     class Meta:
#         ordering = ['-date']
#         verbose_name_plural = 'Attendance'

#     @property
#     def user_in(self):
#         return f'{self.time_in.all().first().time_in} {TimeStatus.TIME_IN[0][0]}'

#     @property
#     def user_out(self):
#         return f'{self.time_out.all().first().time_out} {TimeStatus.TIME_OUT[1][0]}'
