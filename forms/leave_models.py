from django.db import models    
from django.db.models.signals import post_save
from django.dispatch import receiver

# from users.models import User
from api.choices import Leave, Status
from django.contrib.auth import get_user_model
from extras.models import LeaveCounter
from trackers.models import LeaveTracker

User = get_user_model()


class LeaveForm(models.Model):
    leave_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='leaves')
    
    class Meta:
        abstract = True
     
class LeaveRequestForm(LeaveForm):
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    # Admin can only view this
    status = models.CharField(max_length=10, choices=Status, default='Pending')
    leave_type = models.CharField(max_length=50, choices=Leave)

    approved_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='approved_leaves', null=True, blank=True)  # Admin can only view this
    approved_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.leave_user}'

    @property
    def vacation(self):
        if self.leave_type == 'Vacation Leave':
            vacation_leave = LeaveCounter.vacation_leave
            self.save()
            return int(vacation_leave)

    @property
    def sick(self):
        if self.leave_type == 'Sick Leave':
            sick_leave = LeaveCounter.sick_leave
            self.save()
            return int(sick_leave)
        
    @property
    def number_of_days(self):
        return int((self.end_date - self.start_date).days)
    
    @property
    def number_of_leaves(self):
        if self.leave_type == 'Vacation Leave':
            return int(self.vacation)
        elif self.leave_type == 'Sick Leave':
            return int(self.sick)
        
    @property
    def remaining_leaves(self):
        return int(self.number_of_leaves - self.number_of_days)

@receiver(post_save, sender=LeaveRequestForm)
def update_leave_tracker(sender, instance, created, **kwargs):
    if created:
        # Update LeaveCounter
        leave_counter = LeaveCounter.objects.first()
        leave_counter.vacation_leave -= instance.number_of_days
        leave_counter.save()

        # Update LeaveTracker
        LeaveTracker.objects.create(
            user=instance.leave_user,
            date_of_leave=instance.start_date,
            to_date=instance.end_date,
            reason=instance.description,
            total_vacation=leave_counter.vacation_leave,
            vacation_leave=True
        )