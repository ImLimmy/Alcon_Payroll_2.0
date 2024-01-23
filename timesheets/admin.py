from django.contrib import admin
from .models import TimeInOut, TimeSheet, TimeLogs

# Register your models here.


class TimeInOutInline(admin.TabularInline):
    model = TimeInOut
    extra = 0


class TimeSheetInline(admin.TabularInline):
    model = TimeSheet
    extra = 0


@admin.register(TimeSheet)
class TimeSheetAdmin(admin.ModelAdmin):
    inlines = [TimeInOutInline]
    list_display = ['user', 'date']


admin.site.register(TimeLogs)
