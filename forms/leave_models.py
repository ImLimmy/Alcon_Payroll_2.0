from django.db import models
from django.conf import settings

from api.choices import Leave, Status
from extras.models import LeaveCounter
# from timesheets_v2.models import TimeSheetV2


class LeaveForm(models.Model):
    leave_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='leave_form')

    class Meta:
        abstract = True


class LeaveRequestForm(LeaveForm):
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    leave_type = models.CharField(max_length=255, choices=Leave)

    status = models.CharField(
        max_length=255, choices=Status, default='Pending')
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='approved_leaves', null=True, blank=True)
    approved_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.leave_user}'

    @property
    def total_hours(self):
        return int((self.end_date - self.start_date).seconds / 3600)

    @property
    def vacation(self):
        if self.leave_type == 'Vacation Leave':
            vacation_leave = LeaveCounter.vacation_leave
            remaining_vacation = vacation_leave - self.total_hours
            self.save()
            return int(remaining_vacation)

    @property
    def sick(self):
        if self.leave_type == 'Sick Leave':
            sick_leave = LeaveCounter.sick_leave
            remaining_sick = sick_leave - self.total_hours
            self.save()
            return f'remaining leave: {int(remaining_sick)}'


class HalfDayForm(models.Model):
    half_day_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='half_days')

    class Meta:
        abstract = True


class HalfDayRequestForm(HalfDayForm):
    form = models.CharField(
        max_length=255, choices=Leave, default='Half Day Leave')
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    status = models.CharField(
        max_length=255, choices=Status, default='Pending')
    approved_by = models.ForeignKey(
        # Admin can only view this
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='approved_half_days', null=True, blank=True)
    approved_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.half_day_user}'

    @property
    def half_day(self):
        if self.form == 'Half Day Leave':
            half_day = LeaveCounter.vacation_leave
            remaining_half_day = half_day - self.shift.total_hours
            self.save()
            return f'remaining leave: {int(remaining_half_day)}'

    @property
    def total_hours(self):
        return int((self.end_date - self.start_date).seconds / 3600)


class UnderTimeForm(models.Model):
    under_time_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='under_times')

    class Meta:
        abstract = True


class UnderTimeRequestForm(UnderTimeForm):
    form = models.CharField(max_length=255, choices=Leave, default='Undertime')
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    status = models.CharField(
        max_length=255, choices=Status, default='Pending')
    approved_by = models.ForeignKey(
        # Admin can only view this
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='approved_under_times', null=True, blank=True)
    approved_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.under_time_user}'

    @property
    def under_time(self):
        if self.form == 'Undertime':
            under_time = LeaveCounter.vacation_leave
            remaining_under_time = under_time - self.total_hours
            self.save()
            return f'remaining leave: {int(remaining_under_time)}'

    @property
    def total_hours(self):
        return int((self.end_date - self.start_date).seconds / 3600)
