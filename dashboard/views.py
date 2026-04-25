from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
from django.shortcuts import render, redirect
from courses.models import Enrollment, ModuleProgress, Course, TestAttempt

def student_dashboard(request):
    if request.user.user_type != 'student':
        return redirect('login')
    enrollments = Enrollment.objects.filter(student=request.user)

    data = []

    for enrollment in enrollments:
        course = enrollment.course
        modules = course.modules.all()

        total_modules = modules.count()
        completed_modules = ModuleProgress.objects.filter(
            student=request.user,
            module__in=modules,
            completed=True
        ).count()

        progress = 0
        if total_modules > 0:
            progress = (completed_modules / total_modules) * 100

        data.append({
            'course': course,
            'progress': progress
        })

    return render(request, 'dashboard/student_dashboard.html', {
        'data': data
    })




def admin_dashboard(request):
    if request.user.user_type != 'admin':
        return redirect('login')
    total_students = User.objects.filter(user_type='student').count()
    total_courses = Course.objects.count()
    total_attempts = TestAttempt.objects.count()
    passed_attempts = TestAttempt.objects.filter(passed=True).count()

    pass_rate = 0
    if total_attempts > 0:
        pass_rate = (passed_attempts / total_attempts) * 100

    return render(request, 'dashboard/admin_dashboard.html', {
        'students': total_students,
        'courses': total_courses,
        'attempts': total_attempts,
        'pass_rate': pass_rate
    })