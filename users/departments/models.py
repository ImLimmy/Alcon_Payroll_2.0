from django.db import models
from django.db.models import F

# Create your models here.

class Department(models.Model):
    
    department = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        # Either of the 2 can be used
        
        # ordering = ["-id"]
        ordering = ["id"]
        
        # ordering = [F('id').desc(nulls_last=True)]
        # ordering = [F('id').asc(nulls_last=True)]
    
    def __str__(self):
        return f"{self.department}" #self.department
   