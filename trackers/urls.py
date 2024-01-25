from . import views
from django.urls import path

urlpatterns = [
    # http://127.0.0.1:8000/alcon_payroll/trackers/leave_tracker/
    path('leave_tracker/', views.LeaveTrackerList.as_view(), name='leave_tracker_list'),
    path('leave_tracker/<int:pk>/', views.LeaveTrackerDetail.as_view(), name='leave_tracker_detail'),

    # http://127.0.0.1:8000/alcon_payroll/trackers/leave_tracker/create/
    path('leave_tracker/create/', views.LeaveTrackerList.as_view(), name='leave_tracker_create'),
]