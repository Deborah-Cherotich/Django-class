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
from api.serializers import MinimalClassPeriodSerializer
from api.serializers import MinimalStudentSerializer
from api.serializers import MinimalCourseSerializer
from api.serializers import MinimalRoomsSerializer
from api.serializers import MinimalTeacherSerializer
    
    
class StudentListView(APIView):
    def get(self,request):
        Students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            Students= Students.filter(first_name=first_name)
        country = request.query_params.get("country")
        if country:
           country= Students.filter(country=country)
        serializer = StudentSerializer(country,many=True)
        serializer = MinimalStudentSerializer(Students, many = True)

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
    
     def enroll(self, student, course_id):
        course = Courses.objects.get(id = course_id)
        student.courses.add(course)
        
     def unenroll(self, student, course_id):
        course = Courses.objects.get(id=course_id)
        student.courses.remove(course)
        
     def add_to_class(self, student, class_id):
        student_class = Student.objects.get(id=class_id)
        student_class.students.add(student)

                
     def post(self, request,id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
        if action=="email":
            course_id = request.data.get("course_id")
            self.enroll(student, course_id) 
        return Response(status=status.HTTP_201_CREATED)
    
    
    
     

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
        serializer = MinimalRoomsSerializer(room, many = True)
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
        serializer = MinimalClassPeriodSerializer(period, many = True)
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
    
     def post(self, request, id):
        action = request.data.get("action")
        if action == "create_class_period":
            teacher_id = request.data.get("teacher_id")
            course_id = request.data.get("course_id")
            self.create_class_period(teacher_id, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "get_timetable":
            self.get_timetable(id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

     def create_classPeriod(self, teacher_id, course_id):
        teacher = Teacher.objects.get(id=teacher_id)
        course = Courses.objects.get(id=course_id)
        class_period = Period(teacher=teacher, course=course)
        class_period.save()
        return Response(status=status.HTTP_201_CREATED)
    
     def get_timetable(self, request, id):
        class_period = Period.objects.get(id=id)
        timetable = []
        for day in range(7):  
            day_timetable = []
            for period in class_period.periods.filter(day=day):
                day_timetable.append({
                    'start_time': period.start_time,
                    'end_time': period.end_time,
                    'course': period.courses.name,
                    'teacher': period.teacher.name,
                    'student_class': period.student_class.name
                })
            timetable.append(day_timetable)
        return Response({'timetable': timetable})
    
    
class CoursesListViews(APIView):
    def get(self,request):
        Periods = Courses.objects.all()
        serializer = CoursesSerializer(Periods,many=True)
        serializer = MinimalCourseSerializer(Periods, many = True)
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
        serializer = MinimalTeacherSerializer(Teacher, many = True)
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
    
    def assign_course(self, teacher, course_id):
        course = Courses.objects.get(id=course_id)
        teacher.courses.add(course)
    def assign_class(self, teacher, class_id):
        student_class = Student.objects.get(id=class_id)
        student_class.teacher = teacher
        student_class.save()
        
    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_course":
            course_id = request.data.get("course_id")
            self.assign_course(teacher, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "assign_class":
            class_id = request.data.get("class_id")
            self.assign_class(teacher, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
    class weekelyTimetable(APIView):
      def get(self, request):
        class_periods = Period.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)