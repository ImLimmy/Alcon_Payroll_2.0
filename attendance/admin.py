from django.contrib import admin
from .models import TimeInput

# class TimeInTabularInline(admin.TabularInline):
#     model = TimeInput
#     extra = 1

# class TimeOutTabularInline(admin.TabularInline):
#     model = TimeOut
#     extra = 1

# @admin.register(Attendance)
# class AttendanceAdmin(admin.ModelAdmin):
#     inlines = [TimeInTabularInline, TimeOutTabularInline]
#     list_display = ['user', 'date', 'user_in', 'user_out']
