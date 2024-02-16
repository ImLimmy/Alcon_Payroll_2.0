from django.db import models

# Create your models here.

class Payroll(models.Model):
    get_start_date = models.DateField()
    get_end_date = models.DateField()
    pass

