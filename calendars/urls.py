from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/alcon_payroll/calendars/events/
    path('events/', views.EventList.as_view(), name='calendar_event_list_create'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='calendar_event_retrieve_update_destroy'),

    # http://127.0.0.1:8000/alcon_payroll/calendars/events/create/
    path('events/create/', views.EventCreate.as_view(), name='calendar_event_create'),

    # http://127.0.0.1:8000/alcon_payroll/calendars/events/populate/
    path('events/populate/', views.PopulateCalendarEvents.as_view(), name='populate_holidays'),
]