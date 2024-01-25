from django.db import models


class CalendarEvent(models.Model):
    event = models.CharField(max_length=100)
    date = models.DateField()
    label = models.CharField(null=True, default='', max_length=100)
    
    is_regular_holiday = models.BooleanField(default=True)
    is_special_non_working_holiday = models.BooleanField(default=False)
    is_special_working_holiday = models.BooleanField(default=False)
    is_company_mandated_unpaid = models.BooleanField(default=False)
    is_company_mandated_paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']
        verbose_name_plural = 'Calendar Events'

    def __str__(self):
        return f'{self.event}'

    @property
    def date_str(self):
        return self.date.strftime('%Y-%m-%d')