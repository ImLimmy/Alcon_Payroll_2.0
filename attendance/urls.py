from . import views
from django.urls import path

urlpatterns = [

    # http://127.0.0.1:8000/alcon_payroll/attendance/logs/
    path('logs/', views.AttendanceList.as_view(), name='attendance_list'),
    path('logs/<int:pk>/', views.AttendanceDetail.as_view(),
         name='attendance_detail'),

    # http://127.0.0.1:8000/alcon_payroll/attendance/time-in/
    path('time-in/', views.TimeInList.as_view(), name='time_in'),
    path('time-in/<int:pk>/', views.TimeInDetail.as_view(), name='time_in'),

    # http://127.0.0.1:8000/alcon_payroll/attendance/time-out/
    path('time-out/', views.TimeOutList.as_view(), name='time_out'),
    path('time-out/<int:pk>/', views.TimeOutDetail.as_view(), name='time_out'),
]
