from django.db import models
from users.models import User

class LeaveCounter(models.Model):
    vacation_leave = models.IntegerField(default=5, null=False, blank=False)


class LeaveTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_leave = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    
    approved_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_approved', null=True, blank=True
    )
    approved_date = models.DateField(null=True, blank=True)

    # Renamed from 'vacation' to 'total_vacation'
    total_vacation = models.SmallIntegerField(default=5)
    vacation_leave = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_of_leave']
        verbose_name_plural = 'Leave Tracker'

    @property
    def list_of_users(self):
        return f'{self.user} - {self.date_covered}'
      
    @property
    def date_covered(self):
        return f'{self.date_of_leave} - {self.to_date}'

    @property
    def unused_vacation(self):
        return self.total_vacation - self.total_used_vacation  # Calculate unused vacation

    @property
    def total_used_vacation(self):
        # Calculate total used vacation days for the user

        return LeaveTracker.objects.filter(user=self.user, vacation_leave=True).count()
