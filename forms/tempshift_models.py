from django.db import models

from users.models import User
from api.choices import Status
from shift.models import BreakTemplate

class TemporaryShiftForm(models.Model):
    tempshift_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tempshift_users')
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    
    # Admin can only view this
    status = models.CharField(max_length=10, choices=Status, default='Pending')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.tempshift_user}'
    
    @property
    def schedule(self):
        return f'{self.start_time.strftime("%I:%M %p")} - {self.end_time.strftime("%I:%M %p")}'
    
    @property
    def shift_time(self):
        return f'{self.start_time.strftime("%I:%M %p")} - {self.end_time.strftime("%I:%M %p")}'
    
    @property
    def shift_breaks(self):
        return [f'{break_obj.break_start_time.strftime("%I:%M %p")} - {break_obj.break_end_time.strftime("%I:%M %p")}' for break_obj in Break.objects.filter(shift=self)]
    
class Break(BreakTemplate):
    temporary_break = models.ForeignKey(TemporaryShiftForm, on_delete=models.CASCADE, related_name='temporary_breaks')