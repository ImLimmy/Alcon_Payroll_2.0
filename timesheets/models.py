from django.db import models
from django.utils import timezone
from datetime import time
import pandas as pd

from api.choices import TimeStatus
from users.models import User

class TimeSheet(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='time_sheets')
    date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Time Sheets'
        

class TimeInOut(models.Model):
    time_in = models.TimeField() # first in
    time_out = models.TimeField() # last out
    date = models.ForeignKey(TimeSheet, on_delete=models.CASCADE, related_name='time_in_out')
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Time In Out'
        
    def __str__(self):
        return f'{self.time_in} - {self.time_out}'
        
        