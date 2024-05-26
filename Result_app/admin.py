from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Session)
admin.site.register(Session_Result)
admin.site.register(Education)


class Course_Result_Admin(admin.ModelAdmin):
    list_filter = [
        'student',
        'course',
        'semester',
        'session',
        'score',
        'grade_point',
        'total_point',
        'letter_grade',
    ]

class Semester_Result_Admin(admin.ModelAdmin):
    list_filter = [
        'student',
        'semester',
        'session',
        'gpa',
    ]


admin.site.register(Course_Result, Course_Result_Admin)
admin.site.register(Semester_Result, Semester_Result_Admin)
