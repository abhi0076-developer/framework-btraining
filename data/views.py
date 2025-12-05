from django.shortcuts import render, redirect
from .forms import StudentForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save to the Student table
            return redirect('data:success')
    else:
        form = StudentForm()
    return render(request, 'data/add_student.html', {'form': form})

def success(request):
    return render(request, 'data/success.html')
