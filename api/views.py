from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from room.models import Room
from .serializers import RoomsSerializer
from .serializers import ClassPeriodSerializer
from classPeriod.models import Period
from course.models import Course
from .serializers import CoursesSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
    

class StudentListView(APIView):
    def get(self,request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students,many=True)
        return Response(serializer.data)

class RoomListView(APIView):
    def get(self,request):
        Room = Room.objects.all()
        serializer = RoomsSerializer(Room,many=True)
        return Response(serializer.data)
    
class ClassPeriodListView(APIView):
    def get(self,request):
        Periods = Period.objects.all()
        serializer = ClassPeriodSerializer(Periods,many=True)
        return Response(serializer.data)
    
class CoursesListView(APIView):
    def get(self,request):
        Periods = Course.objects.all()
        serializer = CoursesSerializer(Periods,many=True)
        return Response(serializer.data)
    
class TeacherListView(APIView):
    def get(self,request):
        Teachers = Teacher.objects.all()
        serializer = TeacherSerializer(Teachers, many=True)
        return Response(serializer.data)