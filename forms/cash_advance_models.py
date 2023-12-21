from django.db import models

from users.models import User
from api.choices import Status

class PaymentTerm(models.Model):
    term = models.IntegerField(default=0, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.name
    
class CashAdvanceForm(models.Model):
    cash_advance_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cash_advance_users')
    date = models.DateField(auto_now_add=True)
    cash_amount = models.FloatField(default=0.0, null=False, blank=False)
    payment_term = models.ForeignKey(PaymentTerm, on_delete=models.SET_NULL, null=True, blank=False) # Monthly Amortization
    description = models.TextField(null=False, blank=False)
    
    # Admin can only view this
    status = models.CharField(max_length=10, choices=Status)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.cash_advance_user}'
    
    @property
    def deduction(self):
       return round((self.cash_amount / self.payment_term.term), 2) 
   
    @property
    def remaining_amount(self):
        return round((self.cash_amount - self.deduction), 2)