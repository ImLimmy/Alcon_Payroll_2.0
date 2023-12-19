from django.urls import path, include

urlpatterns = [
    # users app
    path('users/', include('users.urls')),
    
    # calendars app
    path('calendar/', include('calendars.urls')),
    
    # careers app
    path('careers/', include('careers.urls')),
]