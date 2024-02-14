# from django.contrib import admin

# # Register your models here.
# from .models import OTFormV2, TimeSheetV2


# class OTForm_V2Inline(admin.TabularInline):
#     model = OTFormV2
#     extra = 0

# @admin.register(OTFormV2)
# class OTFormV2Admin(admin.ModelAdmin):
#     list_display = ('ts_v2', 'from_time', 'to_time', 'total_hours')


# @admin.register(TimeSheetV2)
# class TimeSheetV2Admin(admin.ModelAdmin):
#     list_display = ('user', 'date', 'time_in', 'time_out', 'hours_work',
#                     'hours_ot', 'regular_pay', 'ot_pay', 'total_pay')
    
#     inlines = [OTForm_V2Inline]