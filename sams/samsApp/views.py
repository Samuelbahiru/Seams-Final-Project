from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import User, Dept, Class, Student, Attendance, Course, Teacher, Assign, AttendanceTotal, time_slots, DAYS_OF_WEEK, AssignTime, AttendanceClass, StudentCourse, NotificationTeacher, NotificationStudent
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# from .forms import TeacherCustomUserCreationForm,AdminCustomUserCreationForm, StudentCustomUserCreationForm, StudentForm, ClassForm, DeptForm, NotificationStudentForm,  NotificationTeacherForm, ClassForm, CourseForm 
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home_view(request):
    return render(request, 'index.html')




def login_view(request): 
    if request.method == 'POST':
        email = request.POST['email']
        passwd = request.POST['password']
        if not (email and passwd):
            messages.error(request, 'Please provide all the details!!')
            return render(request, 'login_page.html')
        user = authenticate(request, email=email, password=passwd)
        if not user:
            messages.error(request, 'Invalid Login Credentials!!')
            return render(request, 'login_page.html')
        if user is not None:
            login(request, user)
        if user.approved:
            if user.is_student:
                return redirect('student_home_url')
            elif user.is_teacher:
                return redirect('teacher_home_url')
        else:
            messages.warning(request,'Your account has not been approved by admin.')
    return render(request, 'login_page.html')

def logoutview(request):
    logout(request)
    return redirect('login_url')



def register_view(request):
    if request.user.is_authenticated:
        return redirect('login_url')
    else:
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + str(user) )
                return redirect('login_url')
        context = {'form':form, 'message': messages}
    return render(request, 'registration.html', context)


# student view

@login_required()
def student_view(request):
    return render(request, 'student_home.html')

@login_required()
def student_attendance(request, stud_id):
    stud = Student.objects.get(USN=stud_id)
    ass_list = Assign.objects.filter(class_id_id=stud.class_id)
    att_list = []
    for ass in ass_list:
        try:
            a = AttendanceTotal.objects.get(student=stud, course=ass.course)
        except AttendanceTotal.DoesNotExist:
            a = AttendanceTotal(student=stud, course=ass.course)
            a.save()
        att_list.append(a)
    return render(request, 'student_attendance.html', {'att_list': att_list})


@login_required()
def student_attendance_detail(request, stud_id, course_id):
    stud = get_object_or_404(Student, USN=stud_id)
    cr = get_object_or_404(Course, id=course_id)
    att_list = Attendance.objects.filter(course=cr, student=stud).order_by('date')
    return render(request, 'student_attendance_detail.html', {'att_list': att_list, 'cr': cr})

@login_required()
def student_notification(request, student_id):
    studentNote = NotificationStudent.objects.filter(student_id=student_id)
    return render(request, 'student_notification.html', {'studentNote':studentNote})
 


# Teacher Views

@login_required()
def teacher_view(request):
    return render(request, 'teacher_home.html')

@login_required
def t_clas(request, teacher_id):
    teacher1 = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teacher_class.html', {'teacher1': teacher1})


@login_required()
def t_student(request, assign_id):
    ass = Assign.objects.get(id=assign_id)
    att_list = []
    for stud in ass.class_id.student_set.all():
        try:
            a = AttendanceTotal.objects.get(student=stud, course=ass.course)
        except AttendanceTotal.DoesNotExist:
            a = AttendanceTotal(student=stud, course=ass.course)
            a.save()
        att_list.append(a)
    return render(request, 'teacher_student.html', {'att_list': att_list})


@login_required()
def t_class_date(request, assign_id):
    now = timezone.now()
    ass = get_object_or_404(Assign, id=assign_id)
    att_list = ass.attendanceclass_set.order_by('date')
    return render(request, 'teacher_class_date.html', {'att_list': att_list})



@login_required()
def t_attendance(request, ass_c_id):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    ass = assc.assign
    c = ass.class_id
    context = {
        'ass': ass,
        'c': c,
        'assc': assc,
    }
    return render(request, 'teacher_attendance.html', context)


@login_required()
def edit_att(request, ass_c_id):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    cr = assc.assign.course
    att_list = Attendance.objects.filter(attendanceclass=assc, course=cr)
    context = {
        'assc': assc,
        'att_list': att_list,
    }
    return render(request, 'teacher_edit_attendance.html', context)


@login_required()
def confirm(request, ass_c_id):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    ass = assc.assign
    cr = ass.course
    cl = ass.class_id
    for i, s in enumerate(cl.student_set.all()):
        status = request.POST[s.USN]
        if status == 'present':
            status = 'True'
        else:
            status = 'False'
        if assc.status == 1:
            try:
                a = Attendance.objects.get(course=cr, student=s, date=assc.date, attendanceclass=assc)
                a.status = status
                a.save()
            except Attendance.DoesNotExist:
                a = Attendance(course=cr, student=s, status=status, date=assc.date, attendanceclass=assc)
                a.save()
        else:
            a = Attendance(course=cr, student=s, status=status, date=assc.date, attendanceclass=assc)
            a.save()
            assc.status = 1
            assc.save()

    return HttpResponseRedirect(reverse('t_class_date_url', args=(ass.id,)))



@login_required()
def t_notification(request, teacher_id):
    note = NotificationTeacher.objects.filter(teacher_id=teacher_id)
    return render(request, 'teacher_notification.html', {'note':note})
    

