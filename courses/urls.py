from django.urls import path
from .views import course_list, course_detail, module_detail, enroll_course, attempt_test, enrolled_courses

urlpatterns = [
    path('', course_list, name='course_list'),
    path('<int:course_id>/', course_detail, name='course_detail'),
    path('module/<int:module_id>/', module_detail, name='module_detail'),

    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
    path('test/<int:module_id>/', attempt_test, name='attempt_test'),
    path('enrolled/', enrolled_courses, name='enrolled_courses'),
]