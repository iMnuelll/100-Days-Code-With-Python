# Basic For Loop
fruits = ["Apple", "Banana", "Peach"]
a = 0
for x in fruits :
    print(f"{a + 1}. {x}")
    a+=1

# Average Age with For Loop
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_heights = 0
for height in student_heights :
  total_heights += height
print(f"total height = {total_heights}")

total_students = 0
for students in student_heights :
  total_students += 1
print (f"number of students = {total_students}")

average = total_heights / total_students
print(f"average height = {round(average)}")

# Highest Score
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest_score = 0
for score in student_scores :
  if score > highest_score :
    highest_score = score
print(f"The highest score in the class is: {highest_score}")

# Adding Even Number
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
jumlah = 0
for i in range (1, target+1) :
    if i % 2 == 0 :
        jumlah += i
print(jumlah)