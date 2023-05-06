# CS50W
CS50 Web Final Project
# Distinctiveness and Complexity
This application is entitled School Registration System. This is a simple web-based application developed in Python and Django Framework. The main purpose of this simple project is to provide a certain school with an online platform to manage, store, and retrieve the students' list. This application allows the school management to register and manage the data of the students. It has a simple and pleasant user interface using the Bootstrap Framework and CoreUI Admin Template. It consists of user-friendly features and functionalities that give the end-user a better experience while using the app. Moreover, all of the web application is responsive to the different screen sizes (mainly mobile phones and computers).This application stores and manage the list of classes, sections, shifts, student list, department, subjects, and teachers. Each of these contains CRUD (Create, Read, Update, and Delete) operations. Some of the said features are available on the actual website while some of it is only accessible at the Django Admin Panel.
# Files Used
- In views.py there is all the backend information of teachers, students and the employees of the school.The main functions are:
  - Students personal information, father's, mother's name, their phone numbers, their grade number etc.
  - Teachers personal information, the subject they teach in the school
  - Employees working in the school
- In models.py there are various models added, to name a few:
  - Class TeacherInfo
  - Class TeacherDeptInfo
  - Class StudentClassInfo
  - Class StudentSectionInfo
  - Class StudentInfo
  - Class StudentShiftInfo
- Various JavaScript files for frontend work
- Templates for all of the different html pages explained above 
- A css file with all of the css used in the web application. 
- Other less important files like urls, admin, settings, static images...
# How To Run The Application
- Install project dependencies by running pip install -r requirements.txt
- Make and apply migrations by running python manage.py makemigrations and python manage.py migrateThis School Registration 
# Features
- Login
- Dashboard
- Student Class Management (Django Admin Panel Only)
  - Register New Class
  - List All Classes
  - Edit Class Details
  - Delete Class
- Student Section Management (Django Admin Panel Only)
  - Register New Section
  - List All Sections
  - Edit Section Details
  - Delete Section
-  Student Shift Management (Django Admin Panel Only)
   -  Register New Shift
   -  List All Shifts
   -  Edit Shift Details
   -  Delete Shift
 -  Student Management
    - Register New Student
    - List All Students
    - View Student Details
    - Edit Student Details
    - Delete Student
 -  Teachers Department Management (Django Admin Panel Only)
     -  Register New Department
     -  List All Departments
     -  Edit Department Details
     -  Delete Department
 -  Teachers Subject Management (Django Admin Panel Only)
     -  Register New Subject
     -  List All Subjects
     -  Edit Subject Details
     -  Delete Subject
 -  Teacher Management
     -   Register New Teacher
     -  List All Teachers
     -  View Teacher Details
     -  Edit Teacher Details
     -  Delete Teacher
 -  Logout
Thanks!
