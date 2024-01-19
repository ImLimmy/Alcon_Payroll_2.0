from django.contrib import admin
from .models import TimeInOut, TimeSheet

# Register your models here.

class TimeInOutInline(admin.TabularInline):
    model = TimeInOut
    extra = 1
    
class TimeSheetInline(admin.TabularInline):
    model = TimeSheet
    extra = 1
    
@admin.register(TimeSheet)
class TimeSheetAdmin(admin.ModelAdmin):
    inlines = [TimeInOutInline]
    list_display = ['user', 'date']