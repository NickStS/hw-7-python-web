from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Group, Teacher, Student, Subject, Grade, engine

fake = Faker()

Session = sessionmaker(bind=engine)
session = Session()

groups = [Group(name='CORE {}'.format(i)) for i in range(1, 4)]
session.add_all(groups)
session.commit()

teachers = [Teacher(name='GOIT {}'.format(i)) for i in range(1, 4)]
session.add_all(teachers)
session.commit()

students = []
for i in range(1, 31):
    group = fake.random_element(groups)
    student = Student(name='student {}'.format(i), group=group)
    students.append(student)
session.add_all(students)
session.commit()

subjects = [Subject(name='Python', teacher=teachers[0]),
            Subject(name='SQL', teacher=teachers[0]),
            Subject(name='HTML', teacher=teachers[1]),
            Subject(name='CSS', teacher=teachers[1]),
            Subject(name='JAVA', teacher=teachers[2])]
session.add_all(subjects)
session.commit()

for student in students:
    for subject in subjects:
        for _ in range(fake.random_int(min=1, max=20)):
            grade = Grade(student=student, subject=subject, grade=fake.random_int(min=2, max=5), date=fake.date_between(start_date='-6M', end_date='today'))
            session.add(grade)
session.commit()

print("Data seeding completed.")
