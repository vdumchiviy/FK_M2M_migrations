from django.contrib import admin

from .models import Student, Teacher
from .models import TeacherStudent


class TeacherStudentInline(admin.TabularInline):
    model = TeacherStudent


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [TeacherStudentInline]


# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
