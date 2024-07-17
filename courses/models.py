from django.db import models
from datetime import datetime

class Courses(models.Model):
    course = models.CharField(max_length=20, primary_key=True)
    course_id = models.SmallIntegerField()
    department = models.CharField(max_length=20)
    course_description = models.TextField()
    class_starting_time = models.TimeField(default="00:00:00")
    course_instructor = models.CharField(max_length=28)
    number_of_students = models.PositiveSmallIntegerField()
    grade_level = models.PositiveSmallIntegerField()
    school_term = models.IntegerField()
    assessment_requirements = models.TextField()
    course_trainer_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.course} ({self.course_trainer_name})"