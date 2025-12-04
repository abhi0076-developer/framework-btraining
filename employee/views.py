from django.shortcuts import render,redirect
from .forms import EmployeeForm
# Create your views here.
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form=EmployeeForm()
    return render(request,'add_employee.html',{'form':form})

def success(request):
    return render(request,"success.html")

# Create your views here.
