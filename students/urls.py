from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='students_list'),
    path('students/new/', views.student_form, name='student_form'),
    path('students/edit/<int:student_id>', views.student_update, name='student_edit'),
    path('students/delete/<int:student_id>/', views.student_delete, name='student_delete'),
    path('', views.course_list, name='courses_list'),
    path('courses/new/', views.course_form, name='course_form'),
    path('courses/edit/<int:course_id>/', views.course_edit, name='course_edit'),
    path('courses/delete/<int:course_id>/', views.course_delete, name='course_delete'),
    path('courses/search/',views.course_search,name='course_search'),
    path('students/search/',views.student_search,name='student_search')
]
