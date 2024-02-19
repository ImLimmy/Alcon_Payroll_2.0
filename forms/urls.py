from . import views
from django.urls import path

urlpatterns = [

    # http://127.0.0.1:8000/alcon_payroll/forms/cash_advance/
    path('cash_advance/', views.CashAdvanceList.as_view(),
         name='cash_advance_list'),
    path('cash_advance/<int:pk>/', views.CashAdvanceDetail.as_view(),
         name='cash_advance_detail'),

    # http://127.0.0.1:8000/alcon_payroll/forms/cash_advance/create/
    path('cash_advance/create/', views.CashAdvanceList.as_view(),
         name='cash_advance_create'),

    # http://127.0.0.1:8000/alcon_payroll/forms/half_day/
    path('half_day/', views.HalfDayList.as_view(), name='half_day_list'),
    path('half_day/<int:pk>/', views.HalfDayDetail.as_view(), name='half_day_detail'),


    # http://127.0.0.1:8000/alcon_payroll/forms/leave/
    path('leave/', views.LeaveList.as_view(), name='leave_list'),
    path('leave/<int:pk>/', views.LeaveDetail.as_view(), name='leave_detail'),

    # http://127.0.0.1:8000/alcon_payroll/forms/leave/create/
    path('leave/create/', views.LeaveList.as_view(), name='leave_create'),

    # http://127.0.0.1:8000/alcon_payroll/forms/overtime/
    path('overtime/', views.OverTimeList.as_view(), name='overtime_list'),
    path('overtime/<int:pk>/', views.OverTimeDetail.as_view(),
         name='overtime_detail'),

    # http://127.0.0.1:8000/alcon_payroll/forms/overtime/create/
    path('overtime/create/', views.OverTimeList.as_view(), name='overtime_create'),

    # http://127.0.0.1:8000/alcon_payroll/forms/kpi/
    path('kpi/', views.KpiList.as_view(), name='kpi_list'),
    path('kpi/<int:pk>/', views.KpiDetail.as_view(), name='kpi_detail'),

    # http://127.0.0.1:8000/alcon_payroll/forms/kpi/create/
    path('kpi/create/', views.KpiList.as_view(), name='kpi_create'),

    # http://127.0.0.1:8000/alcon_payroll/forms/temporary_shift/
    path('temporary_shift/', views.TemporaryShiftList.as_view(),
         name='temporary_shift_list'),
    path('temporary_shift/<int:pk>/', views.TemporaryShiftDetail.as_view(),
         name='temporary_shift_detail'),

    # http://127.0.0.1:8000/alcon_payroll/forms/temporary_shift/create/
    path('temporary_shift/create/', views.TemporaryShiftList.as_view(),
         name='temporary_shift_create'),
]
