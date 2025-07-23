# 🎓 Django Students & Courses Management System

A complete Django-based web application for managing students and courses. This project allows users to **add, view, update, delete**, and **search** for courses and students. The UI is built with **Bootstrap**, and features include **form validation**, **pagination**, and a **responsive design**.

---

## 🚀 Features

### 🧾 Course Management
- **Create Course**: Add a new course with name and description.
- **Update Course**: Edit existing course details.
- **Delete Course**: Remove a course from the database.
- **Validation**: Prevents blank names and duplicates using Django's `clean_name()` method.

### 👨‍🎓 Student Management
- **Create Student**: Add a student with name, email, gender, and phone number.
- **Update Student**: Edit student details.
- **Delete Student**: Delete a student record.
- **Validation**: Ensures proper email format and non-empty fields.

### 🔍 Search Functionality
- **Search Courses**: Users can search by course name using a search bar.
- The form submits a GET request and filters results based on the query.
- Displays “No results found” if no matches exist.

### 📄 Pagination
- Course list supports pagination.
- Navigation includes: `« Prev` | page numbers | `Next »`
- Disabled buttons if no more pages.

### 🎨 User Interface
- Clean UI with **Bootstrap** and **Font Awesome** icons.
- Styled buttons (Add, Edit, Delete) with hover effects.
- Table view for listing data with alternating row colors and hover highlight.
- Responsive design for desktops and tablets.

---

## 🗂️ Project Structure

students_task/
│
├── students/ # Django app
│ ├── models.py # Models for Course and Student
│ ├── forms.py # Django forms with validation
│ ├── views.py # Core logic for rendering and form handling
│ ├── urls.py # URL patterns for student/course views
│ └── templates/
│ └── ...html # Templates for displaying pages
│

├── db.sqlite3 # SQLite database
├── manage.py # Django project manager

