student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades ={}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores :
  grades =""
  if student_scores[student] >= 91 or student_scores[student] == 100 :
    grades = "Outstanding"
  elif student_scores[student] >= 81 or student_scores[student] == 90 :
    grades = "Exceeds Expectations"
  elif student_scores[student] >= 71 or student_scores[student] == 80 :
    grades = "Acceptable"
  elif student_scores[student] <= 70 :
    grades = "Fail"
  student_grades[student] = grades

# 🚨 Don't change the code below 👇
for student in student_scores :
  print(f"{student}: {student_grades[student]}")