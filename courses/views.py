from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from accounts.utils import is_admin

@login_required
def course_list(request):
    if not is_admin(request.user):
        return redirect('no_access')

    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})


@login_required
def course_add(request):
    if not is_admin(request.user):
        return redirect('no_access')

    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('course_list')

    return render(request, 'courses/form.html', {'form': form})


@login_required
def course_edit(request, pk):
    if not is_admin(request.user):
        return redirect('no_access')

    course = get_object_or_404(Course, id=pk)
    form = CourseForm(request.POST or None, instance=course)

    if form.is_valid():
        form.save()
        return redirect('course_list')

    return render(request, 'courses/form.html', {'form': form})


@login_required
def course_delete(request, pk):
    if not is_admin(request.user):
        return redirect('no_access')

    course = get_object_or_404(Course, id=pk)
    course.delete()
    return redirect('course_list')
