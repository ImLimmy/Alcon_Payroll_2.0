from django.contrib import admin
from .kpi_models import Kpi
from .leave_models import LeaveRequestForm, HalfDayRequestForm, UnderTimeRequestForm
from .call_approval_forms import CashAdvanceForm, From_to, TemporaryShiftForm, OverTimeForm, PaymentTerm


@admin.register(PaymentTerm)
class PaymentTermAdmin(admin.ModelAdmin):
    list_display = ('term', 'name')
    list_filter = ('term', 'name')

@admin.register(CashAdvanceForm)
class CashAdvanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'cash_amount',
                    'payment_term', 'deduction', 'status')
    list_filter = ('user', 'date', 'payment_term', 'status')


@admin.register(HalfDayRequestForm)
class HalfDayAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'status')
    list_filter = ('user', 'start_date', 'end_date', 'status')


@admin.register(UnderTimeRequestForm)
class UnderTimeAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'status')
    list_filter = ('user', 'start_date', 'end_date', 'status')

@admin.register(Kpi)
class KpiAdmin(admin.ModelAdmin):
    list_display = ('category', 'metrics', 'min_score',
                    'max_score', 'remarks', 'comments')


# @admin.register(LeaveForm)
# class LeaveAdmin(admin.ModelAdmin):
#     list_display = ('leave_user', 'days', 'leave_type', 'status')
#     list_filter = ('leave_user', 'status')

@admin.register(LeaveRequestForm)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'description', 'status')
    list_filter = ('user', 'status')


class OTInline(admin.TabularInline):
    model = From_to
    extra = 1

@admin.register(OverTimeForm)
class OverTimeAdmin(admin.ModelAdmin):
    list_display = ('date', 'status')
    list_filter = ('date', 'status')
    inlines = [OTInline]


@admin.register(TemporaryShiftForm)
class TemporaryShiftAdmin(admin.ModelAdmin):
    list_display = ('user', 'schedule',
                    'shift_time', 'shift_breaks', 'status')
    list_filter = ('user', 'status')
