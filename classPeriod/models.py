from django.db import models
from datetime import datetime

class Period(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='periods')
    classroom = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='periods')
    day_of_the_week = models.DateField()

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"