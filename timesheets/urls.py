from . import views
from django.urls import path

urlpatterns = [

    # http://127.0.0.1:8000/alcon_payroll/timesheets/
    path('', views.TimeSheetList.as_view(), name='timesheet_list'),

]
