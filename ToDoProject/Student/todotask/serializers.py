from pyexpat import model
from rest_framework import serializers
 
from .models import Course, Category, Student

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'category_name',
        )

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        course = CategorySerializer(many=True, read_only=True)
        model = Course
        fields = (
            'course_name',
            'course_description',
            'category',
        )

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        course = CourseSerializer(many=True, read_only=True)
        model = Student
        fields = (
            'name',
            'number',
            'course',
        )


