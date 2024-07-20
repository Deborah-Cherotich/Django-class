from django.shortcuts import render
from rest_framework import status
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from room.models import Room
from .serializers import RoomsSerializer
from .serializers import ClassPeriodSerializer
from  classPeriod.models import Period
from courses.models import Courses
from .serializers import CoursesSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
    
    
class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetailView(APIView):
     def get(self,request,id):
        student  = Student.objects.get(id = id)
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data)
    
     def put (self,request,id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
     def delete(self,request,id):
        student = Student.objects.get(id = id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED) 
       

class RoomListView(APIView):
    def get(self,request):
        room = Room.objects.all()
        serializer = RoomsSerializer(room,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = RoomsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
     
class RoomDetailView(APIView):
     def get(self,request,id):
        room  = Room.objects.get(id = id)
        serializer = RoomsSerializer(room, many = True)
        return Response(serializer.data)
    
     def put (self,request,id):
        room = Room.objects.get(id = id)
        serializer = RoomsSerializer(room,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
     def delete(self,request,id):
        room = Room.objects.get(id = id)
        room.delete()
        return Response(status=status.HTTP_202_ACCEPTED) 
    
 
class ClassPeriodListView(APIView):
    def get(self,request):
        period = Period.objects.all()
        serializer = ClassPeriodSerializer(period,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ClassPeriodSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
        
class ClassPeriodDetailView(APIView):
     def get(self,request,id):
        period  = Period.objects.get(id = id)
        serializer = RoomsSerializer(period, many = True)
        return Response(serializer.data)
    
     def put (self,request,id):
        period = Period.objects.get(id = id)
        serializer = ClassPeriodSerializer(period,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
     def delete(self,request,id):
        period = Period.objects.get(id = id)
        period.delete()
        return Response(status=status.HTTP_202_ACCEPTED) 
    
    
    
class CoursesListView(APIView):
    def get(self,request):
        Periods = Courses.objects.all()
        serializer = CoursesSerializer(Periods,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CoursesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
        
class CoursesDetailView(APIView):
    def get(self,request,id):
        course  = Courses.objects.get(id = id)
        serializer = CoursesSerializer(course, many = True)
        return Response(serializer.data)
    
    def put (self,request,id):
        course = Courses.objects.get(id = id)
        serializer = CoursesSerializer(course,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        course = Courses.objects.get(id = id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED) 
    
class TeacherListView(APIView):
    def get(self,request):
        Teachers = Teacher.objects.all()
        serializer = TeacherSerializer(Teachers, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
        
class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher, many = True)
        return Response(serializer.data)
    
    def put (self,request,id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        teacher = Teacher.objects.get(id = id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED) 