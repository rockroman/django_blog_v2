from .models import Employee
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .forms import EmployeeForm


# Create your views here.
def employee_data(request):
    employees = Employee.objects.all()
    template_name = "employees.html"
    context = {"employees": employees}

    return render(request, "employee/employees.html", {"employees": employees})


def add_employee(request):
    form = EmployeeForm
    return render (request,"employee/add_employee.html",{"form":form})


# class EmployeesList(generic.ListView):
#     template_name = "employees.html"
#     model = Employee
#     queryset = Employee.objects.all()
#     context_object_name = "employees"
