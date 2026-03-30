import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facial_attendance.settings')
django.setup()

from accounts.models import User
from academics.models import Faculty, AcademicClass, Student
from django.utils import timezone

def setup_demo_data():
    print("Setting up demo data...")

    # 1. Create Faculty
    faculty, _ = Faculty.objects.get_or_create(
        name="Science & Technology",
        defaults={'description': 'Main engineering faculty'}
    )

    # 2. Create Admin
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'first_name': 'System',
            'last_name': 'Admin',
            'email': 'admin@example.com',
            'role': 'admin',
            'is_staff': True,
            'is_superuser': True,
        }
    )
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        print("Created Admin: admin / admin123")
    else:
        print("Admin user already exists.")

    # 3. Create Teacher
    teacher_user, created = User.objects.get_or_create(
        username='teacher1',
        defaults={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'teacher@example.com',
            'role': 'teacher',
        }
    )
    if created:
        teacher_user.set_password('teacher123')
        teacher_user.save()
        print("Created Teacher: teacher1 / teacher123")
    else:
        print("Teacher user already exists.")

    # 4. Create Class
    academic_class, _ = AcademicClass.objects.get_or_create(
        name="Computer Science - Year 1",
        faculty=faculty,
        defaults={'teacher': teacher_user}
    )

    # 5. Create Student User
    student_user, created = User.objects.get_or_create(
        username='student1',
        defaults={
            'first_name': 'Alice',
            'last_name': 'Smith',
            'email': 'student@example.com',
            'role': 'student',
        }
    )
    if created:
        student_user.set_password('student123')
        student_user.save()
        print("Created Student User: student1 / student123")
    else:
        print("Student user already exists.")

    # 6. Create Student Profile
    student_profile, created = Student.objects.get_or_create(
        user=student_user,
        defaults={
            'full_name': 'Alice Smith',
            'enrollment_year': 2025,
            'faculty': faculty,
            'academic_class': academic_class,
            'phone': '9876543210',
        }
    )
    if created:
        print("Created Student Profile for Alice Smith")

    print("\n--- Setup Complete ---")
    print("Admin:   admin / admin123")
    print("Teacher: teacher1 / teacher123")
    print("Student: student1 / student123")

if __name__ == "__main__":
    setup_demo_data()
