from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    
    # http://127.0.0.1:8000/alcon_payroll/users/
    path('', views.UserList.as_view(), name='user_list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    
    # http://127.0.0.1:8000/alcon_payroll/users/departments/
    path('departments/', views.DepartmentList.as_view(), name='department_list'),
    path('departments/<int:pk>/', views.DepartmentDetail.as_view(), name='department_detail'),
    
    # http://127.0.0.1:8000/alcon_payroll/users/login/
    path('login/', obtain_auth_token, name='login'),

    # http://127.0.0.1:8000/alcon_payroll/users/logout/
    path('logout/', views.Logout.as_view(), name='logout'),
        
    # http://127.0.0.1:8000/alcon_payroll/users/positions/
    path('positions/', views.PositionList.as_view(), name='position_list'),
    path('positions/<int:pk>/', views.PositionDetail.as_view(), name='position_detail'),
    
    # http://127.0.0.1:8000/alcon_payroll/users/register/
    path('register/', views.Register.as_view(), name='register'),
]