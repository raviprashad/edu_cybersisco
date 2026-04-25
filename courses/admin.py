from django.contrib import admin

# Register your models here.
from .models import Course, Module, StudyMaterial


class StudyMaterialInline(admin.TabularInline):
    model = StudyMaterial
    extra = 1


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1

class ModuleAdmin(admin.ModelAdmin):
    inlines = [StudyMaterialInline]
    list_display = ['title', 'course', 'order']

class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]
    list_display = ['title', 'created_by', 'is_published', 'created_at']
    list_filter = ['is_published']
    search_fields = ['title'] 

admin.site.register(Course, CourseAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(StudyMaterial)


from .models import Enrollment, ModuleProgress

admin.site.register(Enrollment)
admin.site.register(ModuleProgress)


from .models import Test, Question, Option, TestAttempt

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(TestAttempt)