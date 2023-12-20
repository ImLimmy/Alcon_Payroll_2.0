from django.urls import path, include

urlpatterns = [
    # attendance app
    path('attendance/', include('attendance.urls'), name='attendance'),
    
    # calendars app
    path('calendar/', include('calendars.urls'), name='calendar'),
    
    # careers app
    path('careers/', include('careers.urls'), name='careers'),
    
    # forms app
    path('forms/', include('forms.urls'), name='forms'),
    
    # shift app
    path('shift/', include('shift.urls'), name='shift'),
    
    # users app
    path('users/', include('users.urls'), name='users'),
    
]