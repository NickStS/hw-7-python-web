from faker import Faker
import random
import psycopg2

fake = Faker()

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="123"
)

cursor = connection.cursor()

for _ in range(3):
    group_name = fake.word().capitalize()
    cursor.execute("INSERT INTO groups (name) VALUES (%s)", (group_name,))

for _ in range(3):
    teacher_name = fake.name()
    cursor.execute("INSERT INTO teachers (name) VALUES (%s)", (teacher_name,))

for _ in range(30):
    student_name = fake.name()
    group_id = random.randint(1, 3)
    cursor.execute("INSERT INTO students (name, group_id) VALUES (%s, %s)", (student_name, group_id))

for _ in range(5):
    subject_name = fake.word().capitalize()
    teacher_id = random.randint(1, 3)
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)", (subject_name, teacher_id))

for student_id in range(1, 31):
    for subject_id in range(1, 6):
        grade = random.randint(2, 5)
        date = fake.date_between(start_date='-6M', end_date='today')
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (%s, %s, %s, %s)",
                       (student_id, subject_id, grade, date))

connection.commit()
connection.close()
