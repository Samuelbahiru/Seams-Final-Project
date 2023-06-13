from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User
# from .models import User, Dept, Class, Student, Attendance, Course, Teacher, Assign, AttendanceTotal, time_slots, DAYS_OF_WEEK, AssignTime, AttendanceClass, StudentCourse, NotificationStudent, NotificationTeacher
from django.forms import ModelForm



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name','last_name','email','is_teacher','is_student')

        
# class TeacherForm(ModelForm):
#     class Meta:
#         model = Teacher
#         fields = '__all__'
        
# class StudentForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = '__all__'

# class ClassForm(ModelForm):
#     class Meta:
#         model = Class
#         fields = '__all__'

# class DeptForm(ModelForm):
#     class Meta:
#         model = Dept
#         fields = '__all__'

# class NotificationStudentForm(ModelForm):
#     class Meta:
#         model = NotificationStudent
#         fields = '__all__'   

# class NotificationTeacherForm(ModelForm):
#     class Meta:
#         model = NotificationTeacher
#         fields = '__all__'  

# class CourseForm(ModelForm):
#     class Meta:
#         model = Course
#         fields = '__all__'  

