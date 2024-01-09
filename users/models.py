from collections.abc import Collection
from typing import Any
from django.db import models
from .departments.models import Department
from .positions.models import Position
from careers.models import Careers
from api.choices import Gender, CivilStatus, Suffix, EducationalAttainment
from shift.models import Shift
from contributions.models import (
    PagIbig,
    PhilHealth,
    SSS,
)
from payroll_extras.models import Incentives, Deductions
from forms.kpi_models import Kpi

from django.contrib.auth.models import AbstractUser, UserManager, Group

class Privilege(models.Model):
    privilege = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return f'{self.privilege}'
    
class Permission(models.Model):
    permission = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.permission}'
    
    class Meta:
        abstract = True
    
class PrivilegesPermission(Permission):
    privileges = models.ForeignKey(Privilege, on_delete=models.CASCADE, related_name='privilege_permissions')
    
    class Meta:
        unique_together = ('privileges', 'permission')

class Manager(UserManager):
    def create_user(self,username:str, email:str | None = None, password:str | None = None, **extra_fields: Any) -> Any:
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        email = self.normalize_email(email)
        user =self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username: str, email: str | None, password: str | None, **extra_fields: Any) -> Any:
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)
    
class User(AbstractUser):
    # Login
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, unique=True)
    
    # Profile   
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    suffix = models.CharField(max_length=10, choices=Suffix, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=Gender)
    educational_attainment = models.CharField(max_length=30, choices=EducationalAttainment)
    civil_status = models.CharField(max_length=10, choices=CivilStatus)
    
    # Work Information
    employee_id = models.IntegerField(unique=True, null=True, blank=True)
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True)
    career = models.ForeignKey(Careers, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    privilege = models.ForeignKey(Privilege, on_delete=models.SET_NULL, null=True)
    
    # Salary Information
    salary_per_day = models.FloatField(null=False, blank=False, default=0.0)
    number_of_days = models.IntegerField(null=False, blank=False, default=0)
    
    incentives = models.ManyToManyField(Incentives)
    deductions = models.ManyToManyField(Deductions)
    
    kpi = models.OneToOneField(Kpi, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Contributions
    pag_ibig_number = models.IntegerField(unique=True, null=True, blank=False)
    pag_ibig_contribution = models.ForeignKey(PagIbig, on_delete=models.CASCADE, null=True, blank=True)
    
    philhealth_number = models.IntegerField(unique=True, null=True, blank=False)
    philhealth_contribution = models.ForeignKey(PhilHealth, on_delete=models.CASCADE, null=True, blank=True)
        
    sss_number = models.IntegerField(unique=True, null=True, blank=False)
    sss_contribution = models.ForeignKey(SSS, on_delete=models.CASCADE, null=True, blank=True)
    
    # Permissions
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = Manager()
    
    def __str__(self) -> str:
        return f'{self.get_full_name()}'
    
    def has_module_perms(self, app_label: str) -> bool:
        return self.is_superuser
    
    def has_perms(self, perm_list: Collection[str]) -> bool:
        return self.is_superuser
    
    def get_full_name(self) -> str:
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name} {self.suffix}'
        return f'{self.employee_id} | {self.username}'
    
    # Salary Computation
    @property
    def basic_salary_per_month(self) -> float:
        return round((self.salary_per_day * self.number_of_days), 2)
    
    @property
    def basic_pay(self) -> float:
        return round((self.basic_salary_per_month / 2), 2)
    
    # PagIbig Contribution Computation
    @property
    def pag_ibig_contributions(self) -> float:
        max_value = 0.0
        if self.pag_ibig_contribution is not None:
            if self.basic_salary_per_month > self.pag_ibig_contribution.lower_end:
                if self.basic_salary_per_month < self.pag_ibig_contribution.higher_end:
                    max_value = self.basic_salary_per_month       
                else:
                    max_value = self.pag_ibig_contribution.higher_end
                return round((max_value * self.pag_ibig_contribution.employee_share_higher_bracket) / 100, 2)
            else:
                max_value = self.basic_salary_per_month
            return round((max_value * self.pag_ibig_contribution.employee_share_lower_bracket) / 100, 2)
        return 0
    
    # PhilHealth Contribution Computation
    @property
    def phil_health_contributions(self) -> float:
        if self.philhealth_contribution is None:
            return 0
        
        rate = self.philhealth_contribution.rate
        minimum_salary = self.philhealth_contribution.minimum_salary
        maximum_salary = self.philhealth_contribution.maximum_salary
        
        if self.basic_pay < minimum_salary:
            return 0
        if self.basic_pay > maximum_salary:
            self.basic_pay = maximum_salary
        
        return round((self.basic_pay * rate) / 100, 2)
            
    # SSS Contribution Computation
    @property
    def sss_contributions(self) -> float:
        sss_account = SSS.objects.filter(minimum_salary__lte=self.basic_pay, maximum_salary__gte=self.basic_pay).first()
        if sss_account is None:
            return 0
        return sss_account.aoc_total_employee