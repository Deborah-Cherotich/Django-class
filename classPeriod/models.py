from django.db import models
import datetime
# Create your models here.
class Period(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.CharField(max_length=25)
    day_of_the_week = models.DateField(datetime.date.today)
    course = models.CharField(max_length=25)

 
    def __str__(self):
        return f"{self.course} {self.classroom} {self.start_time}"