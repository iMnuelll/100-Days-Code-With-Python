# If/Else & Conditional Operator
print("Welcome to the rollercoaster!!!")
height = int(input("What is your height in cm? "))

# Conditional Operator : >, <, >=, <=, ==, !=
if height > 120 :
    print("You can ride the rollercoaster")
    # Contoh nested if
    age = int(input("How old are you? "))
    if age < 12 :
       print("You have to pay $5")
    elif age >= 12 and age <= 18 :
       print("You have to pay $7")
    else :
       print("You have to pay $12")
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