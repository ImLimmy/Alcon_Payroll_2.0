from django.db import models

# from users.models import User
from api.choices import Status
from django.contrib.auth import get_user_model
User = get_user_model()


class OverTimeForm(models.Model):
    overtime_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='overtime_users')
    date = models.DateField(auto_now_add=True)
    overtime_hours = models.FloatField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    # Admin can only view this
    status = models.CharField(max_length=10, choices=Status, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.overtime_user}'
