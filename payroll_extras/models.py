from django.db import models

from api.choices import Extras

class Incentives(models.Model):
    incentive_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    incentive_amount = models.FloatField(null=False, blank=False, default=0.0)
    
    # Admin can only view this
    include_in_users = models.BooleanField(default=False, null=False, blank=False)
    incentive_status = models.CharField(max_length=50, choices=Extras)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Incentive'
        verbose_name_plural = 'Incentives'
    
    def __str__(self):
        return f'{self.incentive_name}'

class Deductions(models.Model):
    deduction_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    deduction_amount = models.FloatField(null=False, blank=False, default=0.0)
    
    # Admin can only view this
    include_in_users = models.BooleanField(default=False, null=False, blank=False)
    deduction_status = models.CharField(max_length=50, choices=Extras)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Deduction'
        verbose_name_plural = 'Deductions'
    
    def __str__(self):
        return f'{self.deduction_name}'