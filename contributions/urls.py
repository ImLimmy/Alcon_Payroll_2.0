from . import views
from django.urls import path

urlpatterns = [

    # http://127.0.0.1:8000/alcon_payroll/contributions/pagibig/
    path('pagibig/create/', views.PagIbigList.as_view(), name='pagibig'),
    path('pagibig/<int:pk>/update/',
         views.PagIbigDetail.as_view(), name='pagibig_update'),

    # http://127.0.0.1:8000/alcon_payroll/contributions/philhealth/
    path('philhealth/create/', views.PhilHealthList.as_view(), name='philhealth'),
    path('philhealth/<int:pk>/update/',
         views.PhilHealthDetail.as_view(), name='philhealth_update'),

    # http://127.0.0.1:8000/alcon_payroll/contributions/sss/
    path('sss/create/', views.SSSList.as_view(), name='sss'),
    path('sss/<int:pk>/update/', views.SSSDetail.as_view(), name='sss_update'),

]
