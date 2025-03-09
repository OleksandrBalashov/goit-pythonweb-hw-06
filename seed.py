from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Subject, Teacher, Grade

fake = Faker()

DATABASE_URL = "postgresql://alexandrbalashov:1349@localhost:5432/hw"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()

teachers = [Teacher(name=fake.name()) for _ in range(3)]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=fake.word(), teacher_id=fake.random_element(teachers).id) for _ in range(5)]
session.add_all(subjects)
session.commit()

students = [Student(name=fake.name(), group_id=fake.random_element(groups).id) for _ in range(30)]
session.add_all(students)
session.commit()

grades = [
    Grade(student_id=student.id, subject_id=subject.id, grade=fake.random_element([2, 3, 4, 5]))
    for student in students for subject in subjects
]
session.add_all(grades)
session.commit()

print("Data has been seeded successfully!")
