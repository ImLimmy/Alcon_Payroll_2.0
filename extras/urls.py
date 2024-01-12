from . import views
from django.urls import path

urlpatterns = [

    # http://127.0.0.1:8000/alcon_payroll/extras/incentives/
    path('incentives/', views.IncentivesList.as_view(), name='incentives_list'),
    path('incentives/<int:pk>/', views.IncentivesDetail.as_view(),
         name='incentives_detail'),

    # http://127.0.0.1:8000/alcon_payroll/extras/deductions/
    path('deductions/', views.DeductionsList.as_view(), name='deductions_list'),
    path('deductions/<int:pk>/', views.DeductionsDetail.as_view(),
         name='deductions_detail'),
]
