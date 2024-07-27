import os
import django
from datetime import date

from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student


# 01. Add Students

def add_students() -> None:
    students_to_add = [
        Student(student_id='FC5204', first_name='John', last_name='Doe', birth_date='1995-05-15',
                email='john.doe@university.com'),
        Student(student_id='FE0054', first_name='Jane', last_name='Smith', birth_date=None,
                email='jane.smith@university.com'),
        Student(student_id='FH2014', first_name='Alice', last_name='Johnson', birth_date='1998-02-10',
                email='alice.johnson@university.com'),
        Student(student_id='FH2015', first_name='Bob', last_name='Wilson', birth_date='1996-11-25',
                email='bob.wilson@university.com')
    ]

    Student.objects.bulk_create(students_to_add)


#
# add_students()
# print(Student.objects.all())

# 02. Get Students Info

def get_students_info() -> str:
    return '\n'.join(str(s) for s in Student.objects.all())


# print(get_students_info())

# 03. Update Students' Emails

def update_students_emails():
    students = Student.objects.all()
    for student in students:
        old_email = student.email
        new_email = old_email.replace("university.com", "uni-students.com")
        student.email = new_email
        student.save()


# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)

# 04. Truncate Students
def truncate_students():
    Student.objects.all().delete()


# truncate_students()
# print(Student.objects.all())
# print(f"Number of students: {Student.objects.count()}")
