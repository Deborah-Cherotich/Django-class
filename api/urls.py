from django.urls import path
from .views import StudentListView
from .views import RoomListView
from .views import ClassPeriodListView
from .views import CoursesListView
from .views import TeacherListView



urlpatterns = [
    path(
        "students/",StudentListView.as_view(),name="student_list_view"
    ),
    path(
        "classes/", RoomListView.as_view(), name="class_list_view"
    ),
    path(
        "periods/", ClassPeriodListView.as_view(), name="classPeriod_list_view"
    ),
    path(
        "courses/", CoursesListView.as_view(), name="course_list_view" 
    ),
    path(
        "teachers/", TeacherListView.as_view(), name="teachers_list_view"
    )
]