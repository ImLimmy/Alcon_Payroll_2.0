from django.db import models

from users.models import User
from api.choices import Leave, Status


class LeaveForm(models.Model):
    leave_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='leave_users')
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    # Admin can only view this
    status = models.CharField(max_length=10, choices=Status, default='Pending')
    leave_type = models.CharField(max_length=50, choices=Leave)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.leave_user}'

    @property
    def days(self):
        return (self.end_date - self.start_date).days
