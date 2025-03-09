from sqlalchemy.orm import aliased
from sqlalchemy import func
from sqlalchemy.orm import Session
from models import Student, Grade, Group, Teacher, Subject
from db import session


def select_1():
    result = (
        session.query(Student.name, func.avg(Grade.grade).label("average_grade"))
        .join(Grade, Grade.student_id == Student.id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
        .all()
    )
    return result


def select_2(subject_id):
    result = (
        session.query(Student.name, func.avg(Grade.grade).label("average_grade"))
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .first()
    )
    return result


def select_3(subject_id):
    result = (
        session.query(Group.name, func.avg(Grade.grade).label("average_grade"))
        .join(Group.students)
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .all()
    )
    return result


def select_4():
    result = session.query(func.avg(Grade.grade)).scalar()
    return result


def select_5(teacher_id):
    results = (
        session.query(Subject.name)
        .join(Teacher)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )
    return results


def select_6(group_id):
    results = session.query(Student.name).join(Group).filter(Group.id == group_id).all()
    return results


def select_7(group_id, subject_id):
    results = (
        session.query(Student.name, Grade.grade)
        .join(Group)
        .join(Grade)
        .filter(Group.id == group_id, Grade.subject_id == subject_id)
        .all()
    )
    return results


def select_8(teacher_id):
    grade_alias = aliased(Grade)
    return (
        session.query(func.avg(grade_alias.grade).label("average_grade"))
        .join(Subject, grade_alias.subject_id == Subject.id)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )


def select_9(student_id):
    return (
        session.query(Subject.name.label("subjects_name"))
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Grade.student_id == student_id)
        .all()
    )


def select_10(student_id, teacher_id):
    return (
        session.query(Subject.name.label("subjects_name"))
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
        .all()
    )


def select_11(student_id, teacher_id):
    return (
        session.query(func.avg(Grade.value).label("average_grade"))
        .join(Subject)
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
        .all()
    )
