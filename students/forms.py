from django import forms
from .models import Course, Student
from django.core.exceptions import ValidationError

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']  

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name:
            raise ValidationError("Course name cannot be blank.")
        if not name.isalnum():
            raise ValidationError("Course Name must be in Alphabets Or Numbers")
        
        # if Course.objects.filter(name__iexact=name).exists():
        #     raise forms.ValidationError("Course name must be unique.")
        
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')

        # if not description:
        #     raise ValidationError("Description cannot be blank.")

        return description
    
class StudentForm(forms.ModelForm):


    class Meta:
        model = Student
        fields = ['fname', 'lname', 'email', 'gender', 'phoneno', 'status', 'course']
    
    def clean_course(self):
        course = self.cleaned_data.get('course')
        if not course:
            raise ValidationError("Please select a course.")
        return course

    def clean_fname(self):
        fname = self.cleaned_data.get('fname')
        if not fname:
            raise ValidationError("First name cannot be empty.")
        if not fname.isalpha():
            raise ValidationError("First name must contain only letters.")
        return fname

    def clean_lname(self):
        lname = self.cleaned_data.get('lname')
        if not lname:
            raise ValidationError("Last name cannot be empty.")
        if not lname.isalpha():
            raise ValidationError("Last name must contain only letters.")
        return lname

    def clean_phoneno(self):
        phoneno = self.cleaned_data.get('phoneno')
        if not phoneno:
            raise ValidationError("Phone number is required.")
        if not phoneno.isdigit():
            raise ValidationError("Phone number must contain only digits.")
        if len(phoneno) != 10:
            raise ValidationError("Phone number must be exactly 10 digits.")
        return phoneno

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Email is required.")
        # if Student.objects.filter(email=email).exists():
        #     raise ValidationError("This email is already registered.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        fname = cleaned_data.get('fname')
        lname = cleaned_data.get('lname')
        if fname == lname:
            raise ValidationError("First and last name cannot be the same.")
        return cleaned_data

