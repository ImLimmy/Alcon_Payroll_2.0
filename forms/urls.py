from . import views
from django.urls import path

urlpatterns = [

    # http://127.0.0.1:8000/alcon_payroll/forms/cash_advance/
    path('', views.CashAdvanceList.as_view(), name='cash_advance_list'),
    path('<int:pk>/', views.CashAdvanceDetail.as_view(), name='cash_advance_detail'),
    
    # http://127.0.0.1:8000/alcon_payroll/forms/cash_advance/create/
    path('create/', views.CashAdvanceList.as_view(), name='cash_advance_create'),
    
    # http://127.0.0.1:8000/alcon_payroll/forms/half_day/
    path('', views.HalfDayList.as_view(), name='half_day_list'),
    path('<int:pk>/', views.HalfDayDetail.as_view(), name='half_day_detail'),
    
    # http://127.0.0.1:8000/alcon_payroll/forms/half_day/create/
    path('create/', views.HalfDayList.as_view(), name='half_day_create'),
    
    # http://127.0.0.1:8000/alcon_payroll/forms/leave/
    path('', views.LeaveList.as_view(), name='leave_list'),
    path('<int:pk>/', views.LeaveDetail.as_view(), name='leave_detail'),
    
    # http://127.0.0.1:8000/alcon_payroll/forms/leave/create/
    path('create/', views.LeaveList.as_view(), name='leave_create'),
    
    # http://127.0.0.1:8000/alcon_payroll/forms/overtime/
    path('', views.OverTimeList.as_view(), name='overtime_list'),
    path('<int:pk>/', views.OverTimeDetail.as_view(), name='overtime_detail'),
    
    # http://127.0.0.1:8000/alcon_payroll/forms/overtime/create/
    path('create/', views.OverTimeList.as_view(), name='overtime_create'),
    
    # http://127.0.0.1:8000/alcon_payroll/forms/kpi/
    path('kpi/', views.KpiList.as_view(), name='kpi_list'),
    path('kpi/<int:pk>/', views.KpiDetail.as_view(), name='kpi_detail'),
    
    # http://127.0.0.1:8000/alcon_payroll/forms/kpi/create/
    path('create/', views.KpiList.as_view(), name='kpi_create'),
    
    # http://127.0.0.1:8000/alcon_payroll/forms/temporary_shift/
    path('', views.TemporaryShiftList.as_view(), name='temporary_shift_list'),
    path('<int:pk>/', views.TemporaryShiftDetail.as_view(), name='temporary_shift_detail'),
    
    # http://127.0.0.1:8000/alcon_payroll/forms/temporary_shift/create/
    path('create/', views.TemporaryShiftList.as_view(), name='temporary_shift_create'),
    
]