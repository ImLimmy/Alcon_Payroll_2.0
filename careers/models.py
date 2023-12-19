from django.db import models 

class Careers(models.Model):
    
    CAREER_STATUS = (
        ('Probationary', 'Probationary'),
        ('Contractual', 'Contractual'), ('End of Contract', 'End of Contract'),
        ('Regular', 'Regular'), ('Resigned', 'Resigned'), ('Retired', 'Retired'),
        ('Terminated', 'Terminated'), ('Absent without Leave', 'Absent without Leave'),
    )

    career_status = models.CharField(max_length=100, choices=CAREER_STATUS)
    career_description = models.TextField()
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Careers'

    def __str__(self):
        return self.career_status