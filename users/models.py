from collections.abc import Collection
from typing import Any
from django.db import models
from .departments.models import Department
from .positions.models import Position
from careers.models import Careers
from api.choices import Gender, CivilStatus, Suffix, EducationalAttainment
from shift.models import Shift

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
    
    employee_id = models.IntegerField(unique=True, null=True, blank=True)
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True)
    career = models.ForeignKey(Careers, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    privilege = models.ForeignKey(Privilege, on_delete=models.SET_NULL, null=True)
    
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
    
