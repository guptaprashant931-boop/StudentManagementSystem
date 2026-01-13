from django.db import models
from courses.models import Course
# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    # admission_date = models.DateField(auto_now_add=True)
    # is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    