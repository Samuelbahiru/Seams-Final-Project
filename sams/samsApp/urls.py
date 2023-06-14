from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home_view, name = "home_url"),
    path('login/', views.login_view, name='login_url'),
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
     
   
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_complete_.html'), name='password_reset_complete'),     

]