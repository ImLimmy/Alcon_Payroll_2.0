from django.db import models

from users.models import User
from api.choices import Status

class HalfDayForm(models.Model):
    half_day_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='half_day_users')
    date = models.DateField(auto_now_add=True)
    time_out = models.TimeField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    
    # Admin can only view this
    status = models.CharField(max_length=10, choices=Status, default='Pending')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.half_day_user}'