from django.db import models

class Room(models.Model):
      class_name= models.CharField(max_length=20).primary_key
      class_id = models.PositiveSmallIntegerField(default=2023)
      names_of_teachers = models.TextField(default=2023)
      number_of_enrolled_students = models.PositiveSmallIntegerField(default=2023)
      number_of_classrooms= models.TextField(default=2023)
      meeting_days = models.CharField(max_length=20)
      academic_year = models.PositiveSmallIntegerField(default=2023)
      class_capacity = models.PositiveSmallIntegerField(default=2023)
      name = models.CharField(max_length=25)
      building = models.CharField(max_length=100, default='Main Building')
      capacity = models.IntegerField(default=2023)
      def __str__(self):
        return f"{self.class_name} {self.class_id}"


