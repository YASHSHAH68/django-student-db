from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student
from .forms import CourseForm , StudentForm , StudentCreateForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse
from urllib.parse import urlencode

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
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.status = 'Active'
            student.save()
            return redirect('students_list')
    else:
        form = StudentCreateForm()

    courses = Course.objects.all()
    return render(request, 'student_form.html', {'form': form , 'courses': courses})


def course_list(request):

    query = request.GET.get('query', '')
    try:
        limit = int(request.GET.get('limit', '5'))
    except:
        limit = 5

    courses = Course.objects.all().order_by('-createdAt')

    if query:
        courses = courses.filter(Q(name__icontains=query) | Q(description__icontains=query))

    paginator = Paginator(courses, limit)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'course_list.html', {
        'courses': page_object,
        'page_obj': page_object,
        'limit': limit,
        'query': query,
    })


def student_list(request):
    query = request.GET.get('query')
    try:
        limit = int(request.GET.get('limit' , '5'))
    except:
        limit = 5

    students = Student.objects.all().order_by('-createdAt')

    if query:
        students = students.filter(Q(fname__icontains = query) | Q(lname__icontains = query) | Q(phoneno__icontains = query) | Q(email = query))
    
    paginator = Paginator(students , limit)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'student_list.html', 
                  {'students': page_object ,
                   'page_obj' : page_object , 
                   'limit' : limit , 
                   'query' : query,
                   })

def course_edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    query = request.GET.get('query' , '')
    limit = request.GET.get('limit' , '5')
    page = request.GET.get('page' , '1')

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('courses_list')}?{urlencode({'query': query, 'limit': limit, 'page': page})}")
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form, 'mode' : 'edit' , 'query' : query , 'limit' : limit , 'page' : page})

def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    query = request.GET.get('query' , '')
    limit = request.GET.get('limit', '5')
    page = request.GET.get('page', '1')

    if request.method == 'POST':
        course.delete()
        return redirect(f"{reverse('courses_list')}?{urlencode({'query': query, 'limit': limit, 'page': page})}")

    return render(request, 'confirm_course_deletion.html', {
        'course': course,
        'query': query,
        'limit': limit,
        'page': page,
    })

def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    query = request.GET.get('query' , '')
    limit = request.GET.get('limit' , '5')
    page = request.GET.get('page','1')

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('students_list')}?{urlencode({'query': query, 'limit': limit, 'page': page})}")  
    else:
        form = StudentForm(instance=student)

    courses = Course.objects.all()
    return render(request, 'student_form.html', {'form': form, 'mode' : 'edit', 'courses' : courses , 'query' : query , 'limit' : limit , 'page' : page})

def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    query = request.GET.get('query' , '')
    limit = request.GET.get('limit', '5')
    page = request.GET.get('page', '1')
    if request.method == 'POST':
        student.delete()
        return redirect(f"{reverse('students_list')}?{urlencode({'query': query, 'limit': limit, 'page': page})}")
    
    return render(request, 'confirm_student_deletion.html', {
        'student': student,
        'query': query,
        'limit': limit,
        'page': page,
    })
