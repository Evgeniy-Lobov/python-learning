students = [
    ("Алексей", [4, 3, 5, 4]),
    ("Мария", [5, 5, 4, 5]),
    ("Иван", [3, 3, 4, 4]),
    ("Ольга", [5, 4, 5, 5]),
]

#Перебор списка студентов с использованием enumerate
for index, (name, grades) in enumerate(students, start = 1):
    average_grade = sum(grades) / len(grades)
    print(f"{index}. {name} – Средняя оценка: {average_grade:.5f}")