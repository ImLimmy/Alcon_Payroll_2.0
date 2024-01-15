from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Privilege, PrivilegesPermission, DepartmentPermission, PositionPermission
from .departments.models import Department
from .positions.models import Position


class DepartmentPermissionInline(admin.TabularInline):
    model = DepartmentPermission
    extra = 0


class PositionPermissionInline(admin.TabularInline):
    model = PositionPermission
    extra = 0


class PrivilegesPermissionInline(admin.TabularInline):
    model = PrivilegesPermission
    extra = 0


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('employee_id',
                    'username',
                    'email',
                    'first_name',
                    'last_name',
                    'salary_per_day',
                    'basic_pay',
                    'basic_salary_per_month',
                    'pag_ibig_contributions',
                    'phil_health_contributions',
                    'sss_contributions',
                    )
    fieldsets = (
                ('Login', {'fields': ('username',
                                      'email',
                                      'password')}),
                ('Profile', {'fields': ('image',
                                        'first_name',
                                        'last_name',
                                        'middle_name',
                                        'suffix',
                                        'gender',
                                        'civil_status',
                                        'educational_attainment',
                                        )}),
                ('Work Information', {'fields': ('employee_id',
                                                 'shift',
                                                 'career',
                                                 'department',
                                                 'position',
                                                 )}),
                ('Salary Information', {'fields': ('salary_per_day',
                                                   'number_of_days',
                                                   'incentives',
                                                   'deductions',
                                                   'kpi',
                                                   )}),
                ('Contributions', {'fields': ('pag_ibig_number',
                                              'pag_ibig_contribution',
                                              'philhealth_number',
                                              'philhealth_contribution',
                                              'sss_number',
                                              'sss_contribution',
                                              )}),
                ('Important Dates', {'fields': ('last_login',
                                                'date_joined',)}),
                ('Permissions', {'fields': ('is_staff',
                                            'is_superuser',
                                            'is_active',
                                            'groups',
                                            'user_permissions',
                                            )}),
    )
    list_filter = ('is_staff',
                   'is_superuser',
                   'is_active',)
    search_fields = ('username',
                     'email',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    inlines = (DepartmentPermissionInline,)
    list_display = ['department']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    inlines = (PositionPermissionInline,)
    list_display = ['position']


# admin.site.register(Department)
# admin.site.register(Position)

@admin.register(Privilege)
class RoleAdmin(admin.ModelAdmin):
    inlines = (PrivilegesPermissionInline,)
    list_display = ['privilege']
