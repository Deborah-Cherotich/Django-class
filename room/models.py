from django.db import models

# Create your models here.
class Room (models.Model):
    room_name = models.CharField(max_length=20)
    Duration= models.DurationField(max_length=20)
    year = models.CharField(max_length=20)
    department = models.CharField(max_length=30)
    img = models.ImageField()
    capacity = models.CharField(max_length=50)
    
    
    
    def __str__(self):
        return f"{self.name} {self.Duration} {self.capacity}"