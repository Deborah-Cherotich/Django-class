from django.db import models
# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    gender = models.CharField(default=2023)
    bio = models.TextField(default=2023)
    id_number = models.SmallIntegerField(default=2023)
    code = models.SmallIntegerField(default=2023)
    country = models.CharField(default=2023)
    gurdian_name = models.CharField(default=2023)
    student_next_of_kin = models.CharField(default=2023)
    student_national_id_number = models.CharField(default=2023)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    