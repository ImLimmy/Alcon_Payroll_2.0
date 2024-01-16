from django.contrib import admin
from .cash_advance_models import CashAdvanceForm, PaymentTerm
from .half_day_models import HalfDayForm
from .kpi_models import Kpi
from .leave_models import LeaveForm
from .overtime_models import OverTimeForm
from .tempshift_models import TemporaryShiftForm


@admin.register(CashAdvanceForm)
class CashAdvanceAdmin(admin.ModelAdmin):
    list_display = ('cash_advance_user', 'date', 'cash_amount',
                    'payment_term', 'deduction', 'status')
    list_filter = ('cash_advance_user', 'date', 'payment_term', 'status')


@admin.register(HalfDayForm)
class HalfDayAdmin(admin.ModelAdmin):
    list_display = ('half_day_user', 'date', 'time_out', 'status')
    list_filter = ('half_day_user', 'date', 'status')


@admin.register(Kpi)
class KpiAdmin(admin.ModelAdmin):
    list_display = ('category', 'metrics', 'min_score',
                    'max_score', 'remarks', 'comments')


@admin.register(LeaveForm)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('leave_user', 'days', 'leave_type', 'status')
    list_filter = ('leave_user', 'status')


@admin.register(OverTimeForm)
class OverTimeAdmin(admin.ModelAdmin):
    list_display = ('overtime_user', 'date', 'overtime_hours', 'status')
    list_filter = ('overtime_user', 'date', 'status')


@admin.register(TemporaryShiftForm)
class TemporaryShiftAdmin(admin.ModelAdmin):
    list_display = ('tempshift_user', 'schedule',
                    'shift_time', 'shift_breaks', 'status')
    list_filter = ('tempshift_user', 'status')


admin.site.register(PaymentTerm)
