from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    return redirect('login')

def no_access(request):
    return HttpResponse("You are not authorized")

@login_required
def profile(request):
    return render(request,'accounts/profile.html')


def user_login(request):
    if request.method == "POST":
        user = authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user:
            login(request,user)
            if user.is_superuser:
                return redirect('student_list')
            elif user.groups.filter(name='Teacher').exists():
                return redirect('attendance_list')
            else:
                return redirect('profile')
        return HttpResponse('Invalid credentials')
    
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

