from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm, EmployeeUpdateForm
from .models import Employee

# Display all employees
def home(request):
    employees = Employee.objects.all()
    return render(request, 'employees/home.html', {'employees': employees})

# Add employee
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

# Update employee (salary and designation should not be editable)
def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeUpdateForm(instance=employee)
    return render(request, 'employees/update_employee.html', {'form': form})

# Delete employee
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.delete()
    return redirect('home')
