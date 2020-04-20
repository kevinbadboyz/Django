from django.urls import path, include
from web_app import views
from .views import EmployeeList, EmployeeCreate, EmployeeUpdate, EmployeeDelete, EmployeeDetail
app_name = 'web_app'

urlpatterns = [    
    path('', EmployeeList.as_view(), name = 'employee_list'),
    path('employee_create', EmployeeCreate.as_view(), name = 'employee_create'),
    path('employee_update/<pk>', EmployeeUpdate.as_view(), name = 'employee_update'),
    path('employee_delete/<pk>', EmployeeDelete.as_view(), name = 'employee_delete'),
    path('employee_detail/<pk>', EmployeeDetail.as_view(), name = 'employee_detail'),
]