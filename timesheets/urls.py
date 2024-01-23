from . import views
from django.urls import path
from .views import ProcessPunchRecord

urlpatterns = [

    # # http://127.0.0.1:8000/alcon_payroll/timesheets/
    # path('', views.TimeSheetList.as_view(), name='timesheet_list'),

    # http://127.0.0.1:8000/alcon_payroll/timesheets/process_punch_record/
    path('process_punch_record/', ProcessPunchRecord.as_view(),
         name='process_punch_record'),

]
