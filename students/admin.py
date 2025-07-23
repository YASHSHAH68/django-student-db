from django.contrib import admin
from students.models import Course
from students.models import Student

class Courses_info(admin.ModelAdmin):
    list_display = ('name' , 'description')

admin.site.register(Course , Courses_info)

class Students_info(admin.ModelAdmin):
    list_display = ('fname' , 'lname' , 'email' , 'gender' , 'phoneno' , 'course')

admin.site.register(Student , Students_info)