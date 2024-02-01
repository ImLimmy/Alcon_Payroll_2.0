from django.urls import path, include

urlpatterns = [

    # calendars app
    path('calendar/', include('calendars.urls'), name='calendar'),

    # careers app
    path('careers/', include('careers.urls'), name='careers'),

    # contributions app
    path('contributions/', include('contributions.urls'), name='contributions'),

    # forms app
    path('forms/', include('forms.urls'), name='forms'),

    # payroll_extras app
    path('extras/', include('extras.urls'), name='extras'),

    # shift app
    path('shift/', include('shift.urls'), name='shift'),

    # users app
    path('users/', include('users.urls'), name='users'),
    
    # trackers app
    path('trackers/', include('trackers.urls'), name='trackers'),

    # timesheets app
    path('timesheets/', include('timesheets.urls'), name='timesheets'),
    
]
