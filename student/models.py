from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length = 20)
    bio = models.TextField()
    id_number = models.SmallIntegerField()
    code = models.SmallIntegerField()
    country = models.CharField(max_length=28)
    gurdian_name = models.CharField(max_length = 28)
    student_next_of_kin = models.CharField(max_length = 20)
    student_national_id_number = models.CharField(max_length = 30)
    # phone_number = models.CharField(max_length=15)
    # image = models.ImageField()
    
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    