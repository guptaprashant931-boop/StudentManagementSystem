from django.db import models
from students.models import Student
# Create your models here.

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.student.name} - {self.date}"
    