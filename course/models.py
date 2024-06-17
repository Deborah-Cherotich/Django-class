from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=20)
    Duration= models.DurationField(max_length=20)
    department = models.CharField(max_length=30)
    code = models.SmallIntegerField()
    content = models.TextField(max_length=50)
    
    
    
    def __str__(self):
        return f"{self.name} {self.code} {self.department}"