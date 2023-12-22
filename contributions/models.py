from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models
from datetime import datetime

# PagIbig Account
class PagIbig(models.Model):
    year = models.IntegerField(default=datetime.now().year, unique=True)
    employer_share = models.FloatField(default=0.0)
    employee_share = models.FloatField(default=0.0)
    higher_end = models.FloatField(default=5000)
    lower_end = models.FloatField(default=0.0)
    
    def __str__(self):
        return f'Year: {self.year} | PagIbig Contribution: ER = {self.employer_share}% , EE = {self.employee_share}%'
    
    class Meta:
        verbose_name = 'PagIbig'
        verbose_name_plural = 'PagIbig'

# PhilHealth
class PhilHealth(models.Model):
    year = models.IntegerField(default=datetime.now().year, unique=True)
    minimum_salary = models.FloatField(validators=[MinValueValidator(10_000), MaxValueValidator(100_000)], default=10000, null=False, blank=False)
    maximum_salary = models.FloatField(validators=[MinValueValidator(10_000), MaxValueValidator(100_000)], default=100000, null=False, blank=False)
    rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0, null=False, blank=False)
    
    def __str__(self) -> str:
        return f'Year: {self.year} | Monthly Basic Salary: {self.minimum_salary} - {self.maximum_salary}'
    
    class Meta:
        verbose_name = 'PhilHealth'
        verbose_name_plural = 'PhilHealth'
  
# SSS
class RangeOfCompensation(models.Model):
    year = models.IntegerField(default=datetime.now().year, unique=True)
    employer = models.FloatField(default=9.5)
    employee = models.FloatField(default=4.5)
    
    def __str__(self):
        return f'SSS Range of Compensation: ER = {self.employer} , EE = {self.employee}'
   
class SSS(models.Model):
    employer_employee = models.ForeignKey(RangeOfCompensation, on_delete=models.CASCADE, null=True, blank=True, related_name='sss_range')
    minimum_salary = models.FloatField()
    maximum_salary = models.FloatField()
    
    class Meta:
        verbose_name = 'SSS'
        verbose_name_plural = 'SSS'
        
    def __str__(self) -> str:
        # return f'SSS Range: {self.minimum_salary} - {self.maximum_salary}'
        return f'Year: {self.employer_employee.year} | {self.employer_employee.__str__()}'
    
    # MSC
    # msc = Monthly Salary Contribution
    @property
    def msc_ec(self):
        if self.minimum_salary < 4250:
            return 4000
        if self.minimum_salary > 19750:
            return 20000
        return round((self.minimum_salary + self.maximum_salary) / 2, 2)
    
    @property
    def msc_wisp(self):
        if self.minimum_salary < 20250:
            return 0
        if self.minimum_salary > 29750:
            return 10000
        return round(((self.minimum_salary + self.maximum_salary) / 2) - 20000, 2)

    @property
    def msc_total(self):
        return self.msc_ec + self.msc_wisp
    
    # AOC
    # aoc = Amount of Contribution
    @property
    def aoc_regular_ss_employer(self):
        return round((self.employer_employee.employer * self.msc_ec) / 100, 2)
    
    @property
    def aoc_regular_ss_employee(self):
        return round((self.employer_employee.employee * self.msc_ec) / 100, 2)
    
    @property
    def aoc_regular_ss_total(self):
        return self.aoc_regular_ss_employer + self.aoc_regular_ss_employee
    
    @property
    def aoc_ec_employer(self):
        if self.msc_total <= 14500:
            return 10
        return 30
    
    @property
    def aoc_ec_employee(self):
        return 0
    
    @property
    def aoc_ec_total(self):
        return self.aoc_ec_employer + self.aoc_ec_employee
    
    @property
    def aoc_wisp_employer(self):
        if self.msc_total <= 20000:
            return 0
        return round((self.msc_wisp * self.employer_employee.employer) / 100, 2)

    @property
    def aoc_wisp_employee(self):
        if self.msc_total <= 20000:
            return 0
        return round((self.msc_wisp * self.employer_employee.employee) / 100, 2)
    
    @property
    def aoc_wisp_total(self):
        return self.aoc_wisp_employer + self.aoc_wisp_employee   
    
    @property
    def aoc_total_employer(self):
        return self.aoc_regular_ss_employer + self.aoc_ec_employer + self.aoc_wisp_employer
    
    @property
    def aoc_total_employee(self):
        return self.aoc_regular_ss_employee + self.aoc_wisp_employee
    
    @property
    def aoc_total(self):
        return self.aoc_total_employer + self.aoc_total_employee
     