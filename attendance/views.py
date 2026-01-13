from django.shortcuts import render,redirect
from datetime import date
from .models import Attendance
from students.models import Student
from accounts.utils import is_teacher
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def mark_attendance(request):
    if not is_teacher(request.user):
        return redirect('no_access')
    
    
    students = Student.objects.all()
    
    if request.method == 'POST':
        for student in students:
            status = request.POST.get(str(student.id))
            Attendance.objects.create(
                student = student,
                present = True if status == 'on' else False
            )
        return redirect('student_list')
    
    return render(request, 'attendance/mark_attendance.html', {'students' : students})

