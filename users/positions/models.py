from django.db import models

# Create your models here.
    
class Position(models.Model):
    
    position = models.CharField(max_length=100, unique=True)
    
    class Meta:
        ordering = ['position']
    
    def __str__(self):
        return self.position