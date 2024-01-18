from django.db import models
from django.utils import timezone
from api.choices import TimeStatus

from users.models import User


class TimeLogs(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='time_log_user')
    date = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Time Logs'
        
        

    

class Attendance(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='attendance_user')
    date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Attendance'

    @property
    def user_in(self):
        return f'{self.time_in.all().first().time_in} {TimeStatus.TIME_IN[0][0]}'

    @property
    def user_out(self):
        return f'{self.time_out.all().first().time_out} {TimeStatus.TIME_OUT[1][0]}'



