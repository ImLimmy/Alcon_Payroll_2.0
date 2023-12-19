from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .departments.models import Department
from .positions.models import Position

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
                                        'career',
                                        'department',
                                        'position',
                                        )}),
                ('Important Dates', {'fields': ('last_login',
                                                'date_joined',)}),
                ('Permissions', {'fields': ('is_staff',
                                            'is_superuser',
                                            'is_active',
                                            )}),
    )
    list_filter = ('is_staff',
                   'is_superuser',
                   'is_active',)
    search_fields = ('username',
                     'email',)
    

admin.site.register(Department)
admin.site.register(Position)