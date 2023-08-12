from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models import Student, Grade, Subject, Teacher, Group, engine

Session = sessionmaker(bind=engine)
session = Session()

def query_subjects(student_name=None, teacher_name=None):
    query = session.query(Subject.name)
    if student_name:
        query = query.join(Grade, Grade.subject_id == Subject.id) \
                     .join(Student, Grade.student_id == Student.id) \
                     .filter(Student.fullname == student_name)
    if teacher_name:
        query = query.join(Teacher, Subject.teacher_id == Teacher.id) \
                     .filter(Teacher.name == teacher_name)
    return query.all()

def select_1():
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .outerjoin(Grade, Student.id == Grade.student_id) \
        .group_by(Student.id) \
        .order_by(func.desc('avg_grade')) \
        .limit(5) \
        .all()
    return result

def select_2(student_name, subject_name):
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Student.fullname == student_name, Subject.name == subject_name) \
        .group_by(Student.id) \
        .order_by(func.desc('avg_grade')) \
        .limit(1) \
        .one_or_none()
    return result

def select_3(subject_name):
    result = session.query(Group.name, func.avg(Grade.grade).label('avg_grade')) \
        .join(Student, Group.id == Student.group_id) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Subject.name == subject_name) \
        .group_by(Group.name) \
        .all()
    return result

def select_4():
    result = session.query(func.avg(Grade.grade).label('avg_grade')).scalar()
    return result

def select_5(teacher_name):
    result = session.query(Subject.name) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Teacher.name == teacher_name) \
        .all()
    return result

def select_6(group_name):
    result = session.query(Student.fullname) \
        .join(Group, Student.group_id == Group.id) \
        .filter(Group.name == group_name) \
        .all()
    return result

def select_7(group_name, subject_name):
    result = session.query(Student.fullname, Grade.grade, Grade.date) \
        .join(Group, Student.group_id == Group.id) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Group.name == group_name, Subject.name == subject_name) \
        .all()
    return result

def select_8(teacher_name):
    result = session.query(func.avg(Grade.grade).label('avg_grade')) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Teacher.name == teacher_name) \
        .scalar()
    return result

def select_9(student_name):
    result = session.query(Subject.name) \
        .join(Grade, Grade.subject_id == Subject.id) \
        .join(Student, Grade.student_id == Student.id) \
        .filter(Student.fullname == student_name) \
        .all()
    return result

def select_10(student_name, teacher_name):
    result = session.query(Subject.name) \
        .join(Grade, Grade.subject_id == Subject.id) \
        .join(Student, Grade.student_id == Student.id) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Student.fullname == student_name, Teacher.name == teacher_name) \
        .all()
    return result


if __name__ == '__main__':
    print(select_1())
    print(select_2('Nick', 'Python'))
    print(query_subjects(student_name='Nick'))
    print(query_subjects(teacher_name='GOIT'))
