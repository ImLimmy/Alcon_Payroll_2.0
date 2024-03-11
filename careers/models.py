from django.db import models

from api.choices import Career


class Careers(models.Model):
    career_status = models.CharField(max_length=100, choices=Career)
    career_description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Careers'

    def __str__(self):
        return self.career_status
