from django.db import models
class Course(models.Model):

    class Meta:
        db_table = 'courses'

    name = models.CharField(max_length=20,unique=True)
    description = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now = True)

class Student(models.Model):

    GENDER_CHOICES = [
    ('Male' , 'Male'),
    ('Female' , 'Female'),
    ('Other' , 'Other')
]
    class Meta:
        db_table = 'students'

    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(unique=True,error_messages={'unique':'No Duplicates Allowed'})
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    phoneno = models.CharField(max_length=10,unique=True)
    status = models.CharField(max_length=20 , default="Activate")
    course = models.ForeignKey(Course , on_delete=models.CASCADE , related_name='course_name')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)