from django.urls import path
from .views import StudentListView
from .views import RoomListView
from .views import ClassPeriodListView
from .views import CoursesListView
from .views import TeacherListView
from .views import StudentDetailView
from .views import RoomDetailView
from .views import ClassPeriodDetailView
from .views import TeacherDetailView
from .views import CoursesDetailView






urlpatterns = [
    path(
        "student/",StudentListView.as_view(),name="student_list_view"
    ),
    path(
        "room/", RoomListView.as_view(), name="room_list_view"
    ),
    path(
        "periods/", ClassPeriodListView.as_view(), name="classPeriod_list_view"
    ),
    path(
        "courses/", CoursesListView.as_view(), name="course_list_view" 
    ),
    path(
        "teachers/", TeacherListView.as_view(), name="teachers_list_view"
    ),
    path("student/<int:id>",StudentDetailView.as_view(), name = "Student_Detail_View"),
    
    path("room<int:id>",RoomDetailView.as_view(), name= "Room_Detail_view"
         ),
    path("classPeriod<int:id>", ClassPeriodDetailView.as_view(), name= "Class_Detail_view"
         ),
    path("teacher<int:id>", TeacherDetailView.as_view(), name= "Teacher_Detail_view"
         ),
    path("course<int:id>", CoursesDetailView.as_view(), name= "Courses_Details_View"),
    

]