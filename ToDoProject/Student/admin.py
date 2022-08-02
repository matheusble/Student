from unicodedata import category
from django.contrib import admin

from models import Category, Course, Student


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
            'category_name',
            )

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name',
            'course_description',
            'category',
            )

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('names',
            'number',
            'sector',
            )