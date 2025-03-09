from my_select import (
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10,
)


def test_queries():
    subject_id = 1
    teacher_id = 1
    group_id = 1
    student_id = 1

    # 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    print("5 студентів із найбільшим середнім балом з усіх предметів: ")
    print(select_1())

    # 2. Знайти студента із найвищим середнім балом з певного предмета
    print(f"\nСтудент із найвищим середнім балом з предмета ID {subject_id}: ")
    print(select_2(subject_id))

    # 3. Знайти середній бал у групах з певного предмета
    print(f"\nСередній бал у групах з предмета ID {subject_id}: ")
    print(select_3(subject_id))

    # 4. Знайти середній бал на потоці (по всій таблиці оцінок)
    print("\nСередній бал на потоці (по всій таблиці оцінок): ")
    print(select_4())

    # 5. Знайти які курси читає певний викладач
    print(f"\nЯкі курси читає викладач з ID {teacher_id}: ")
    print(select_5(teacher_id))

    # 6. Знайти список студентів у певній групі
    print(f"\nСписок студентів у групі з ID {group_id}: ")
    print(select_6(group_id))

    # 7. Знайти оцінки студентів у окремій групі з певного предмета
    print(f"\nОцінки студентів у групі {group_id} з предмета {subject_id}:")
    print(select_7(group_id, subject_id))

    # 8. Знайти середній бал, який ставить певний викладач зі своїх предметів
    print(
        f"\nСередній бал, який ставить викладач з ID {teacher_id} зі своїх предметів:"
    )
    print(select_8(teacher_id))

    # 9. Знайти список курсів, які відвідує певний студент
    print(f"\nСписок курсів, які відвідує студент з ID {student_id}:")
    print(select_9(student_id))

    # 10. Список курсів, які певному студенту читає певний викладач
    print(
        f"\nСписок курсів, які студенту з ID {student_id} читає викладач з ID {teacher_id}:"
    )
    print(select_10(student_id, teacher_id))


if __name__ == "__main__":
    test_queries()
