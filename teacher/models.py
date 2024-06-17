from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=28)
    bio = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.department}"