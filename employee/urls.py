from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("company_emp/", views.employee_data, name="employees"),
    path("add_employee/", views.add_employee, name="add_employee"),
    # path("employee/", views.EmployeesList, name="employees"),
]
