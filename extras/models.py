from django.db import models
from datetime import datetime

from api.choices import Extras


class Incentives(models.Model):
    incentive_name = models.CharField(
        max_length=50, unique=True, null=False, blank=False)
    incentive_amount = models.FloatField(null=False, blank=False, default=0.0)

    # Admin can only view this
    include_in_users = models.BooleanField(
        default=False, null=False, blank=False)
    incentive_status = models.CharField(max_length=50, choices=Extras)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Incentive'
        verbose_name_plural = 'Incentives'

    def __str__(self):
        return f'{self.incentive_name}'


class Deductions(models.Model):
    deduction_name = models.CharField(
        max_length=50, unique=True, null=False, blank=False)
    deduction_amount = models.FloatField(null=False, blank=False, default=0.0)

    # Admin can only view this
    include_in_users = models.BooleanField(
        default=False, null=False, blank=False)
    deduction_status = models.CharField(max_length=50, choices=Extras)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Deduction'
        verbose_name_plural = 'Deductions'

    def __str__(self):
        return f'{self.deduction_name}'


class Ratings(models.Model):
    year = models.IntegerField(default=datetime.now().year, unique=False)
    regular_rate = models.FloatField(null=False, blank=False, default=1.0)
    holiday_rate = models.FloatField(null=False, blank=False, default=2.0)
    rest_day = models.FloatField(null=False, blank=False, default=1.3)
    night_rate = models.FloatField(null=False, blank=False, default=1.1)
    overtime_rate = models.FloatField(null=False, blank=False, default=1.25)

    # Admin can only view this
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

    def __str__(self):
        return f'{self.year}'

    @property
    def ordinary_days(self):
        ordinary_day = self.regular_rate
        return round(ordinary_day, 3)

    @property
    def sunday_or_rest_days(self):
        rest_day = self.regular_rate * self.rest_day
        return round(rest_day, 3)

    @property
    def special_nonworking_days(self):
        special_nonwork_day = self.regular_rate * self.rest_day
        return round(special_nonwork_day, 3)

    @property
    def special_nonworking_and_rest_days(self):
        special_nonwork_and_rest_day = self.regular_rate * self.rest_day + 0.2
        return round(special_nonwork_and_rest_day, 3)

    @property
    def double_special_nonworking_days(self):
        double_special_nonwork_day = self.regular_rate * self.rest_day + 0.2
        return round(double_special_nonwork_day, 3)

    @property
    def double_special_nonworking_and_rest_days(self):
        double_special_nonwork_and_rest_day = self.regular_rate * self.rest_day + 0.65
        return round(double_special_nonwork_and_rest_day, 3)

    @property
    def regular_holidays(self):
        regular_holiday = self.regular_rate * self.holiday_rate
        return round(regular_holiday, 3)

    @property
    def regular_holiday_and_rest_days(self):
        regular_holiday_and_rest_day = self.regular_rate * \
            self.holiday_rate * self.rest_day
        return round(regular_holiday_and_rest_day, 3)

    @property
    def double_holidays(self):
        double_holiday = self.regular_rate * \
            self.holiday_rate * (self.holiday_rate / 2)
        return round(double_holiday, 3)

    @property
    def double_holidays_and_rest_days(self):
        double_holiday_and_rest_day = self.regular_rate * self.holiday_rate + \
            (self.holiday_rate / 2) + ((self.rest_day - 1) * 3)
        return round(double_holiday_and_rest_day, 3)

    @property
    def night_shifts(self):
        night_shift = self.regular_rate * self.night_rate
        return round(night_shift, 3)

    @property
    def night_shift_and_special_nonworking_days(self):
        night_shift_and_special_nonworking_day = self.special_nonworking_days * self.night_shifts
        return round(night_shift_and_special_nonworking_day, 3)

    @property
    def night_shift_special_nonworking_and_rest_days(self):
        night_shift_and_special_nonworking_and_rest_day = self.special_nonworking_and_rest_days * self.night_shifts
        return round(night_shift_and_special_nonworking_and_rest_day, 3)

    @property
    def night_shift_and_double_special_nonworking_days(self):
        night_shift_and_double_special_nonworking_day = self.double_holidays_and_rest_days * self.night_shifts
        return round(night_shift_and_double_special_nonworking_day, 3)

    @property
    def night_shift_and_regular_holidays(self):
        night_shift_and_regular_holiday = self.regular_holidays * self.night_rate
        return round(night_shift_and_regular_holiday, 3)

    @property
    def night_shift_regular_holiday_and_rest_days(self):
        night_shift_regular_holiday_and_rest_day = self.regular_holiday_and_rest_days * self.night_rate
        return round(night_shift_regular_holiday_and_rest_day, 3)

    @property
    def night_shift_and_double_holidays(self):
        night_shift_and_double_holiday = self.double_holidays * self.night_rate
        return round(night_shift_and_double_holiday, 3)

    @property
    def night_shift_double_holidays_and_rest_days(self):
        night_shift_double_holidays_and_rest_day = self.double_holidays_and_rest_days * self.night_rate
        return round(night_shift_double_holidays_and_rest_day, 3)

    @property
    def ordinary_and_overtime_days(self):
        ordinary_and_overtime_days = self.regular_rate * self.overtime_rate
        return round(ordinary_and_overtime_days, 3)

    @property
    def rest_day_and_overtime_days(self):
        rest_day_and_overtime_day = self.rest_day * (self.overtime_rate + 0.05)
        return round(rest_day_and_overtime_day, 3)

    @property
    def special_nonworking_day_and_overtime_days(self):
        special_nonworking_day_and_overtime_day = self.special_nonworking_days * \
            (self.overtime_rate + 0.05)
        return round(special_nonworking_day_and_overtime_day, 3)

    @property
    def special_nonworking_rest_day_and_overtime_days(self):
        special_nonworking_rest_day_and_overtime_day = self.special_nonworking_and_rest_days * \
            (self.overtime_rate + 0.05)
        return round(special_nonworking_rest_day_and_overtime_day, 3)

    @property
    def double_special_nonworking_rest_day_and_overtime_days(self):
        double_special_nonworking_rest_day_and_overtime_day = self.double_special_nonworking_days * \
            (self.overtime_rate + 0.05)
        return round(double_special_nonworking_rest_day_and_overtime_day, 3)

    @property
    def regular_holiday_and_overtime_days(self):
        regular_holiday_and_overtime_day = self.regular_holidays * \
            (self.overtime_rate + 0.05)
        return round(regular_holiday_and_overtime_day, 3)

    @property
    def rest_day_night_shift_and_overtime_days(self):
        rest_day_night_shift_and_overtime_day = self.rest_day * \
            self.night_rate * (self.overtime_rate + 0.05)
        return round(rest_day_night_shift_and_overtime_day, 3)

    @property
    def special_nonworking_day_rest_day_night_shift_and_overtime_days(self):
        special_nonworking_day_rest_day_night_shift_and_overtime_day = self.special_nonworking_and_rest_days * \
            self.night_rate * (self.overtime_rate + 0.05)
        return round(special_nonworking_day_rest_day_night_shift_and_overtime_day, 3)

    @property
    def double_special_nonworking_rest_days_night_shift_and_overtime_days(self):
        double_special_nonworking_rest_days_night_shift_and_overtime_day = self.double_special_nonworking_and_rest_days * \
            self.night_rate * (self.overtime_rate + 0.05)
        return round(double_special_nonworking_rest_days_night_shift_and_overtime_day, 4)

    @property
    def regular_holiday_rest_day_night_shift_and_overtime_days(self):
        regular_holiday_rest_day_night_shift_and_overtime_day = self.night_shift_regular_holiday_and_rest_days * \
            (self.overtime_rate + 0.05)
        return round(regular_holiday_rest_day_night_shift_and_overtime_day, 3)

    @property
    def night_shift_and_double_holidays_and_overtime_days(self):
        night_shift_and_double_holidays_and_overtime_day = self.night_shift_and_double_holidays * \
            (self.overtime_rate + 0.05)
        return round(night_shift_and_double_holidays_and_overtime_day, 3)

    @property
    def night_shift_double_holidays_rest_days_and_overtime_days(self):
        night_shift_double_holidays_rest_days_and_overtime_day = self.night_shift_double_holidays_and_rest_days * \
            (self.overtime_rate + 0.05)
        return round(night_shift_double_holidays_rest_days_and_overtime_day, 3)
