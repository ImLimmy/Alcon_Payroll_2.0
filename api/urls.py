from django.urls import path, include

urlpatterns = [
    # attendance app
    path('attendance/', include('attendance.urls'), name='attendance'),
    
    # calendars app
    path('calendar/', include('calendars.urls'), name='calendar'),
    
    # careers app
    path('careers/', include('careers.urls'), name='careers'),
    
    # contributions app
    path('contributions/', include('contributions.urls'), name='contributions'),
    
    # forms app
    path('forms/', include('forms.urls'), name='forms'),
    
    # payroll_extras app
    path('extras/', include('payroll_extras.urls'), name='extras'),
    
    # shift app
    path('shift/', include('shift.urls'), name='shift'),
    
    # users app
    path('users/', include('users.urls'), name='users'),
    
]