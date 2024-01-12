from . import views
from django.urls import path

urlpatterns = [
    # http://127.0.0.1:8000/alcon_payroll/shift/
    path('', views.ShiftList.as_view(), name='shift_list'),
    path('<int:pk>/', views.ShiftDetail.as_view(), name='shift_detail'),

    # http://127.0.0.1:8000/alcon_payroll/shift/create/
    path('create/', views.ShiftList.as_view(), name='shift_create'),

]
