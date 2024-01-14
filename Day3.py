# If/Else & Conditional Operator
print("Welcome to the rollercoaster!!!")
height = int(input("What is your height in cm? "))
bill = 0 
# Conditional Operator : >, <, >=, <=, ==, !=
if height > 120 :
    print("You can ride the rollercoaster")
    # Contoh nested if
    age = int(input("How old are you? "))
    if age < 12 :
       bill = 5
       print(f"Child tickets are ${bill}")
    elif age >= 12 and age < 18 :
       bill = 7
       print(f"Youth tickets are ${bill}")
    elif age >= 45 and age <= 55 :
       bill = 0
       print("Everything is going to be ok. Have a free ride on us!!!")
    else :
       bill = 12
       print(f"Adults tickets are ${bill}")
    want_photos = input("Would you like to take photos? (Y/N) : ")
    if want_photos == "Y" :
       bill += 3
    else :
       bill += 0
    print(f"Your tickets are ${bill}")
else :
    print("Sorry, you can't ride the rollercoaster")

# Mengecek angka ganjil dan genap
# Which number do you want to check?
print("\nMengecek angka ganjil dan genap")
number = int(input("Masukkan angkanya : "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 1 :
  print("This is an odd number.")
else :
  print("This is an even number.")

# BMI 2.0
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_calculation = weight / height**2
if bmi_calculation < 18.5 :
  print (f"Your BMI is {bmi_calculation}, you are underweight.")
elif bmi_calculation > 18.5 and bmi_calculation < 25 :
  print (f"Your BMI is {bmi_calculation}, you have a normal weight.")
elif bmi_calculation >= 25 and bmi_calculation < 30 :
  print(f"Your BMI is {bmi_calculation}, you are slightly overweight.")
elif bmi_calculation > 30 and bmi_calculation < 35 :
  print(f"Your BMI is {bmi_calculation}, you are obese.")
else :
  print(f"Your BMI is {bmi_calculation}, you are clinically obese.")

# Pizza Order
print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? "S", "M", or "L"
add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# Your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")
# Pizza Order

# Love Calculator
print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# Your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
# Love Calculator