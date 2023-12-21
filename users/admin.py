from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Privilege, PrivilegesPermission
from .departments.models import Department
from .positions.models import Position

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
                    'is_staff', 
                    'is_superuser', 
                    'is_active',
                    )
    fieldsets = (
                ('Login', {'fields': ('username',
                                      'email', 
                                      'password')}),
                ('Profile', {'fields': ('first_name',
                                        'last_name',
                                        'middle_name',
                                        'suffix',
                                        'gender',
                                        'civil_status',
                                        'educational_attainment',
                                        'employee_id',
                                        'shift',
                                        'career',
                                        'department',
                                        'position',
                                        'privilege',
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
    

admin.site.register(Department)
admin.site.register(Position)

@admin.register(Privilege)
class RoleAdmin(admin.ModelAdmin):
    inlines = (PrivilegesPermissionInline,)
    list_display = ['privilege']