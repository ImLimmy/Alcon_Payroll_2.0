from django.contrib import admin
from .models import Careers


@admin.register(Careers)
class CareersAdmin(admin.ModelAdmin):
    list_display = ('career_status', 'career_description',
                    'start_date', 'end_date')
    list_filter = ('career_status', 'start_date', 'end_date')
