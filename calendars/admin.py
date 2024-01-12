from django.contrib import admin
from .models import CalendarEvent


@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):

    list_display = ('event', 'date', 'is_regular_holiday', 'is_special_non_working_holiday',
                    'is_special_working_holiday', 'is_company_mandated_unpaid', 'is_company_mandated_paid')
    list_filter = ('is_regular_holiday', 'is_special_non_working_holiday',
                   'is_special_working_holiday', 'is_company_mandated_unpaid', 'is_company_mandated_paid')
