from django.shortcuts import redirect



# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Course, Module, ModuleProgress, Enrollment


def course_list(request):
    courses = Course.objects.filter(is_published=True)
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    is_enrolled = Enrollment.objects.filter(
        student=request.user,
        course=course
    ).exists()

    modules = course.modules.all() if is_enrolled else []

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'modules': modules,
        'is_enrolled': is_enrolled
    })


def module_detail(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    materials = module.materials.all()
    
    print("MATERIALS:", materials)  # DEBUG

    return render(request, 'courses/module_detail.html', {
        'module': module,
        'materials': materials
    })



def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # prevent duplicate enrollment
    if not Enrollment.objects.filter(student=request.user, course=course).exists():
        Enrollment.objects.create(student=request.user, course=course)

    return redirect('course_detail', course_id=course.id)



from .models import Test, Question, Option, TestAttempt, Module


def attempt_test(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    test = get_object_or_404(Test, module=module)
    questions = test.questions.all()

    if request.method == "POST":
        correct = 0
        total = questions.count()

        for question in questions:
            selected = request.POST.get(str(question.id))

            if selected:
                option = Option.objects.get(id=selected)
                if option.is_correct:
                    correct += 1

        # ✅ INSIDE POST BLOCK
        score = (correct / total) * 100
        passed = score >= test.passing_percentage

        TestAttempt.objects.create(
            student=request.user,
            test=test,
            score=score,
            passed=passed
        )

        # mark module complete
        if passed:
            ModuleProgress.objects.update_or_create(
                student=request.user,
                module=module,
                defaults={'completed': True}
            )

        return render(request, 'courses/test_result.html', {
            'score': score,
            'passed': passed
        })

    # GET request
    return render(request, 'courses/attempt_test.html', {
        'module': module,
        'questions': questions
    })




def enrolled_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    courses = [en.course for en in enrollments]

    return render(request, 'courses/enrolled_courses.html', {
        'courses': courses
    })