from pyexpat import model
from statistics import mode
from django.db import models

class Base(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(Base):
    id = models.AutoField(
    primary_key=True
  )
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name



class Course(Base):
    id = models.AutoField(
    primary_key=True
  )
    course_name = models.CharField(max_length=30)
    course_description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.course_name

class Student(Base):
    id = models.AutoField(
    primary_key=True
  )
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name




