from django.urls import path
from . import views
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView
)



urlpatterns = [
    path('', views.home_view, name = "home_url"),
    path('accounts/login/', views.login_view, name='login_url'),
    path('logout/',views.logoutview, name='logout_url'),

    path('register/',views.register_view, name='register_url'), 

    path('student/<slug:stud_id>/attendance/', views.student_attendance, name='student_attendance_url'),
    path('student/<slug:stud_id>/<slug:course_id>/attendance/', views.student_attendance_detail, name='student_attendance_detail_url'),
    path('student/',views.student_view,name='student_home_url'),
    path('student/<slug:student_id>/notification', views.student_notification, name='student_notification_url'),

    path('teacher/',views.teacher_view,name='teacher_home_url'),
    path('teacher/<slug:teacher_id>/', views.t_clas, name='t_clas_url'),
    path('teacher/<int:assign_id>/Students/attendance/', views.t_student, name='t_student_url'),
    path('teacher/<int:assign_id>/ClassDates/', views.t_class_date, name='t_class_date_url'),
    
    path('teacher/<int:ass_c_id>/attendance/', views.t_attendance, name='t_attendance_url'),
    path('teacher/<int:ass_c_id>/Edit_att/', views.edit_att, name='edit_att_url'),
    path('teacher/<int:ass_c_id>/attendance/confirm/', views.confirm, name='confirm_url'),
  
    path('teacher/<slug:teacher_id>/notification', views.t_notification, name='t_notification_url'),
     
   
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('change-password/', views.change_password, name='change_password'),
]