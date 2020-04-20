from django.shortcuts import render
from .models import Employee
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class EmployeeList(ListView):
    model = Employee
    template_name = 'employee_list.html'

class EmployeeCreate(CreateView):
    model = Employee
    fields = ['code', 'name', 'email', 'phone',]
    template_name = 'employee_form.html'
    success_url = reverse_lazy('web_app:employee_list')

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['code', 'name', 'email', 'phone',]
    template_name = 'employee_form.html'
    success_url = reverse_lazy('web_app:employee_list')

class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('web_app:employee_list')

class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
    
