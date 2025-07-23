from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student
from .forms import CourseForm , StudentForm
from django.core.paginator import Paginator

def course_form(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()

    courses = Course.objects.all()
    return render(request, 'student_form.html', {'form': form , 'courses':courses})


def course_list(request):
    courses = Course.objects.all().order_by('-createdAt')
    
    paginator = Paginator(courses , 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'course_list.html', {'courses': page_object, 'page_obj' : page_object})


def student_list(request):
    students = Student.objects.all().order_by('-createdAt')

    paginator = Paginator(students , 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'student_list.html', {'students': page_object ,'page_obj' : page_object})

def course_edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form, 'mode' : 'edit'})

def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('courses_list')
    
    return render(request, 'confirm_course_deletion.html', {'course': course})

def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students_list')  
    else:
        form = StudentForm(instance=student)

    courses = Course.objects.all()
    return render(request, 'student_form.html', {'form': form, 'mode' : 'edit', 'courses' : courses})

def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('students_list')
    
    return render(request, 'confirm_student_deletion.html', {'student': student})

def course_search(request):
    pass
def student_search(request):
    pass


