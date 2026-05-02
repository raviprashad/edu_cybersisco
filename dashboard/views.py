from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from courses.models import (
    Course, Enrollment, ModuleProgress,
    TestAttempt, Module
)

User = get_user_model()


def student_dashboard(request):
    if not request.user.is_authenticated or request.user.user_type != 'student':
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
            progress = round((completed_modules / total_modules) * 100, 1)

        data.append({
            'course': course,
            'progress': progress,
            'completed': completed_modules,
            'total': total_modules,
        })

    return render(request, 'dashboard/student_dashboard.html', {
        'data': data,
        'enrolled_count': len(data),
    })


def admin_dashboard(request):
    if not request.user.is_authenticated or request.user.user_type != 'admin':
        return redirect('login')

    total_students = User.objects.filter(user_type='student').count()
    total_courses = Course.objects.count()
    published_courses = Course.objects.filter(is_published=True).count()
    total_enrollments = Enrollment.objects.count()
    total_attempts = TestAttempt.objects.count()
    passed_attempts = TestAttempt.objects.filter(passed=True).count()
    failed_attempts = total_attempts - passed_attempts

    pass_rate = 0
    if total_attempts > 0:
        pass_rate = round((passed_attempts / total_attempts) * 100, 1)

    # Per-course stats
    courses = Course.objects.all()
    course_stats = []
    for course in courses:
        enrolled = Enrollment.objects.filter(course=course).count()
        modules = course.modules.all()
        completed = ModuleProgress.objects.filter(
            module__in=modules, completed=True
        ).count()
        course_stats.append({
            'course': course,
            'enrolled': enrolled,
            'completed_modules': completed,
        })

    # Recent test attempts
    recent_attempts = TestAttempt.objects.select_related(
        'student', 'test__module__course'
    ).order_by('-attempted_at')[:10]

    return render(request, 'dashboard/admin_dashboard.html', {
        'total_students': total_students,
        'total_courses': total_courses,
        'published_courses': published_courses,
        'total_enrollments': total_enrollments,
        'total_attempts': total_attempts,
        'passed_attempts': passed_attempts,
        'failed_attempts': failed_attempts,
        'pass_rate': pass_rate,
        'course_stats': course_stats,
        'recent_attempts': recent_attempts,
    })