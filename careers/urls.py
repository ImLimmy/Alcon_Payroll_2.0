from . import views
from django.urls import path

urlpatterns = [
    # http://127.0.0.1:8000/alcon_payroll/careers/
    path('', views.CareersList.as_view(), name='careers_list'),
    path('<int:pk>/', views.CareersDetail.as_view(), name='careers_detail'),
    
    # http://127.0.0.1:8000/alcon_payroll/careers/create/
    path('create/', views.CareersList.as_view(), name='careers_create'),
]