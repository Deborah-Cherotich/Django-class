
from rest_framework import serializers
from student.models import Student
from room.models import Room
from classPeriod.models import Period
from course.models import Course
from teacher.models import Teacher

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        
class RoomsSerializer(serializers.ModelSerializer):
        model=Room
        fields="__all__"
        
class ClassPeriodSerializer(serializers.ModelSerializer):
    model= Period
    fields="__all__"
    
class CoursesSerializer(serializers.ModelSerializer):
    model = Course
    fields = "__all__"
    
class TeacherSerializer(serializers.ModelSerializer):
    model=Teacher
    fields = "__all__"