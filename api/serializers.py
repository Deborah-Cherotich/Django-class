
from datetime import date, datetime
from rest_framework import serializers
from student.models import Student
from room.models import Room
from classPeriod.models import Period
from courses.models import Courses
from teacher.models import Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()

    def get_full_name(self, object):
        return f"{object.first_name} {object.last_name}"

    def get_age(self, object):
        if object.date_of_birth:
            today = datetime.now()
        if isinstance(object.date_of_birth, date) and not isinstance(object.date_of_birth, datetime):
            date_of_birth = datetime.combine(object.date_of_birth, datetime.min.time())
        else:
            date_of_birth = object.date_of_birth
        
        age = today - date_of_birth
        return age.days // 365  
    
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'age']    
        
class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields="__all__"
        
        
class MinimalRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name','capacity']
        
class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
      model= Period
      fields="__all__"
      
      
class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ['id', 'name', 'start_time', 'end_time']
    
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
        
class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'name','teacher']
    

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class MinimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self, object):
        return f"{object.first_name} {object.last_name}"
    
    class Meta:
        model = Teacher
        fields = ['id', 'full_name','email']