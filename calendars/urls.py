from . import views
from django.urls import path

urlpatterns = [
    # http://127.0.0.1:8000/alcon_payroll/calendars/events/
    path('events/', views.EventList.as_view(), name='event_list'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event_detail'),

    # http://127.0.0.1:8000/alcon_payroll/calendars/events/create/
    path('events/create/', views.EventCreate.as_view(), name='event_create'),
]
