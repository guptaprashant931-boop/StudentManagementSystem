from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm
# Create your views here.

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students' : students})

def student_add(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/forms.html', {'form' : form})

# def student_update(request,pk):
#     student = Student.objects.get(id=pk)
#     form = StudentForm(request.POST or None, instance=student)
#     if form.is_valid():
#         form.save()
#         return redirect('student_list')
#     return render(request, 'students/form.html',{'form':form})

# def student_delete(request,pk):
#     student = Student.objects.get(id=pk)
#     student.delete()
#     return redirect('student_list')