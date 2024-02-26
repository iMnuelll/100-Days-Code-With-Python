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

for left in range(7) :
    for right in range(left, 7) :
        print(f"[{left}|{right}]", end=" ")
    print()

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_teams in teams :
    for away_teams in teams :
        if home_teams!= away_teams :
            print(f"{home_teams} vs {away_teams}")

# Slicing
def format_phoneNum(phoneNum): 
    areaCode = f"({phoneNum[:3]})"
    exchangeCode = f"{phoneNum[3:6]}"
    lineNum = f"{phoneNum[-4:]}"
    # Take 4 last digit in the number
    return f"{areaCode} {exchangeCode} - {lineNum}"

print(format_phoneNum("1234567890"))

# Recursive
def factorial(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

factorial(5)

# Here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per pound).
#
basket = [
    ("Peaches", 3.0, 2.99),
    ("Pears", 5.0, 1.66),
    ("Plums", 2.5, 3.99)
]


# Calculate the total price for each item (weight times price per pound)
# and add them up to get a subtotal.
#
subtotal = 0.00
for item in basket:
    fruit, weight, unit_price = item
    print(fruit)
    subtotal += (weight * unit_price)


# Now calculate the sales tax and total bill.
#
tax_rate = 0.06625 # 6.625% sales tax in New Jersey
tax_amt = subtotal * tax_rate
total = subtotal + tax_amt


# Print the receipt for the customer.
print("Subtotal:", subtotal)
print("Sales Tax:", tax_amt)
print("Total:", total)