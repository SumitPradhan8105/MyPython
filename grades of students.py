
student_scores = {
    "Sakti": 91,
    "Bithal": 85,
    "Akash": 90,
    "Sumit": 65,
    "Atish": 78,
    "Animesh": 67
}
student_grades = {}
for i in student_scores:
    if student_scores[i] > 90 and student_scores[i] <= 100:
        student_grades[i] = "Outstanding"
    elif student_scores[i] > 80 and student_scores[i] <= 90:
        student_grades[i] = "Exceeds Expectation"
    elif student_scores[i] > 70 and student_scores[i] <= 80:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"

print(student_grades)
