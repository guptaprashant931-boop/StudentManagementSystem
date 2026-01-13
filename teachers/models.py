from django.db import models
from courses.models import Course
# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name