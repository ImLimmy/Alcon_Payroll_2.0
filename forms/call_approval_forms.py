from django.db import models
from django.conf import settings
from datetime import datetime as dtime

from api.choices import Status
from shift.models import BreakTemplate


class Adjustment(models.Model):
    adjustment_user_name = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='adjustment_users')
    status = models.CharField(max_length=10, choices=Status, default='Pending')
    pass


class PaymentTerm(models.Model):
    term = models.IntegerField(default=0, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class CashAdvanceForm(models.Model):
    cash_advance_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cash_advance_users')
    date = models.DateField(auto_now=True)
    cash_amount = models.FloatField(default=0.0, null=False, blank=False)
    payment_term = models.ForeignKey(
        PaymentTerm, on_delete=models.SET_NULL, null=True, blank=False)  # Monthly Amortization
    description = models.TextField(null=False, blank=False)

    # Admin can only view this
    status = models.CharField(max_length=10, choices=Status, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cash_advance_user}'

    @property
    def deduction(self):
        deduction_amount = self.cash_amount / self.payment_term.term
        return round(deduction_amount, 2)

    @property
    def remaining_amount(self):
        if self.cash_amount >= 0.0:
            return round((self.cash_amount - self.deduction), 2)
        else:
            return 0.0


class OverTimeForm(models.Model):

    overtime_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='overtime_users')
    date = models.DateField(auto_now_add=True)

    # Admin can only view this
    status = models.CharField(max_length=10, choices=Status, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.overtime_user}'


class From_to(models.Model):
    ot_form = models.ForeignKey(
        OverTimeForm, on_delete=models.CASCADE, related_name='ot_forms')
    from_time = models.TimeField()
    to_time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f'{self.from_time} - {self.to_time}'

    @property
    def total_hours(self):
        t1 = dtime.strptime(str(self.from_time), '%H:%M:%S')
        t2 = dtime.strptime(str(self.to_time), '%H:%M:%S')

        duration = t2 - t1
        return round((duration.seconds / 3600), 2)


class TemporaryShiftForm(models.Model):
    temporary_shift_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='temporary_shift_users')
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    status = models.CharField(max_length=10, choices=Status, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    temporary_break = models.ForeignKey(
        TemporaryShiftForm, on_delete=models.CASCADE, related_name='temporary_breaks')
