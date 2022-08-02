"""ToDoTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib import admin
from .views import StudentAPIView, StudentsAPIView, CategoryAPIView, CategoriesAPIView, CoursesAPIView, CourseAPIView


urlpatterns = [
    path('students/', StudentsAPIView.as_view(), name='students'),
    path('students/<int:pk>/', StudentAPIView.as_view(), name='students'),
    path('course/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseAPIView.as_view(), name='courses'),
    path('categories/', CategoriesAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='categories'),
]
