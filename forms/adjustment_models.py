from django.db import models

from users.models import User
from api.choices import Status

class Adjustment(models.Model):
    adjustment_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adjustment_users')
    status = models.CharField(max_length=10, choices=Status, default='Pending')
    pass