from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Shift, Break


class BreakInline(admin.TabularInline):
    model = Break
    extra = 1


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('shift_name', 'schedule',
                    'shift_breaks', 'days', 'on_call', 'break_time', 'final_hours')
    fieldsets = (
        ('Shift', {'fields': ('shift_name',
                              'start_time',
                              'end_time',
                              'grace_period',)}),
        ('Work Day', {'fields': ('monday',
                                 'tuesday',
                                 'wednesday',
                                 'thursday',
                                 'friday',
                                 'saturday',
                                 'sunday',)}),
        ('On Call Day', {'fields': ('monday_on_call',
                                    'tuesday_on_call',
                                    'wednesday_on_call',
                                    'thursday_on_call',
                                    'friday_on_call',
                                    'saturday_on_call',
                                    'sunday_on_call',)}),
    )
    inlines = [BreakInline]
