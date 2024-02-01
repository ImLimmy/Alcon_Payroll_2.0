from django.db import models
from datetime import datetime
import holidays


class CalendarEvent(models.Model):
    event = models.CharField(max_length=100)
    unformat_date = models.FloatField()
    label = models.CharField(null=True, default='', max_length=100)
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

    @property
    def unformatted_date(self):
        return self.unformat_date

    @staticmethod
    def populate_calendar_events():
        ph_holidays = holidays.PH(years=[datetime.now().year])
        for date, name in sorted(ph_holidays.items()):
            date = str(date).split('-')
            unformat_date = float("".join(date))

            CalendarEvent.objects.create(
                event=name, unformat_date=unformat_date, is_regular_holiday=True)
