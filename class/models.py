from django.db import models

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=20)
    Duration= models.DurationField(max_length=20)
    department = models.CharField(max_length=30)
    course = models.CharField(max_length=20)
    instructor = models.CharField(max_length=20)
    capacity = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f"{self.name} {self.course} {self.capacity}"