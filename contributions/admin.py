from django.contrib import admin
from .models import (
    PagIbig,
    PhilHealth,
    SSS,
    RangeOfCompensation
)


@admin.register(PagIbig)
class PagIbigAdmin(admin.ModelAdmin):
    list_display = ('pagibig_year', 'employer_share', 'employee_share_lower_bracket',
                    'employee_share_higher_bracket', 'higher_end', 'lower_end')


@admin.register(PhilHealth)
class PhilHealthAdmin(admin.ModelAdmin):
    list_display = ('philhealth_year', 'minimum_salary',
                    'maximum_salary', 'rate')


@admin.register(SSS)
class SSSAdmin(admin.ModelAdmin):
    list_display = (
        'sss_year',
        'minimum_salary',
        'maximum_salary',
        'msc_ec',
        'msc_wisp',
        'msc_total',
        'aoc_regular_ss_employer',
        'aoc_regular_ss_employee',
        'aoc_regular_ss_total',
        'aoc_ec_employer',
        'aoc_ec_employee',
        'aoc_ec_total',
        'aoc_wisp_employer',
        'aoc_wisp_employee',
        'aoc_wisp_total',
        'aoc_total',
    )


class SSSInline(admin.TabularInline):
    model = SSS
    extra = 0


@admin.register(RangeOfCompensation)
class SSSCalculationAdmin(admin.ModelAdmin):
    inlines = [SSSInline]
    list_display = ['__str__']
