from django.contrib import admin
from .models import LeaveTracker


@admin.register(LeaveTracker)
class LeaveTrackerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_of_leave', 'to_date',
                    'reason', 'total_used_vacation', 'unused_vacation')
