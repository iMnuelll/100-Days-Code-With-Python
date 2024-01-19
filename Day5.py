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

