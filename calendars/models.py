from django.db import models
from datetime import datetime, timedelta
import holidays


class CalendarEvent(models.Model):
    event = models.CharField(max_length=100)
    this_date = models.DateField()
    label = models.CharField(null=True, default='blue', max_length=100)
    description = models.TextField(null=True, default='')

    is_regular_holiday = models.BooleanField(default=True)
    is_special_non_working_holiday = models.BooleanField(default=False)
    is_special_working_holiday = models.BooleanField(default=False)
    is_company_mandated_unpaid = models.BooleanField(default=False)
    is_company_mandated_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Calendar Events'

    def __str__(self):
        return f'{self.event}'

    # @property
    # def unformatted_date(self):
    #     return int(self.this_date.timestamp())
