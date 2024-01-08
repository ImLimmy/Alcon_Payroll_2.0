from django.db import models

# Create your models here.

class Department(models.Model):
    
    department = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['department']
    
    def __str__(self):
        return self.department
    