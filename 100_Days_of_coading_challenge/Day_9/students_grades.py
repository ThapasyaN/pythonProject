students_score = {
    "Aana": 81,
    "Moana": 78,
    "Sofia": 99,
    "Maleficent": 78,
    "Silver": 62
}
student_grades = {}
for student in students_score:
    score = students_score[student]
    if score >= 90:
        student_grades[student] = "Outstanding"
    elif score >= 80:
        student_grades[student] = "Exceeds Exceptations"
    elif score >= 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)

