from django.db import models

# Create your models here.

class Payroll(models.Model):
    get_start_date = models.DateField()
    get_end_date = models.DateField()
    pass

    def __str__(self):
        return f'date ranges from {self.get_start_date} to {self.get_end_date}'