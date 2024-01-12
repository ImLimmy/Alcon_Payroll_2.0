from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class Kpi(models.Model):
    category = models.TextField()
    metrics = models.TextField()
    min_score = models.IntegerField(
        default=0, validators=[MinValueValidator(0)])
    max_score = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    remarks = models.TextField()
    comments = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'KPI'
        verbose_name_plural = 'KPI'

    @property
    def checker(self):
        if self.min_score == self.max_score:
            raise ValidationError('Score must not exceed the Weighted score')
