students_num = int(input())
students = {}

for student in range(students_num):
    name, grade = input().split()
    grade = float(grade)
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)
for name, grade in students.items():
    formatted_grades = ' '.join([f"{g:.2f}" for g in grade])
    avg_grade = sum(grade) / len(grade) if grade else 0

    print(f"{name} -> {formatted_grades} (avg: {avg_grade:.2f})")