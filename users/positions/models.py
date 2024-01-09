from django.db import models

# Create your models here.
    
class Position(models.Model):
    
    position = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ["id"]
    
    def __str__(self):
        return f"{self.position}"