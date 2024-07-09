# Data Types
print("Data Types")
a = "Ini String"
b = 7
c = 3.14
d = 123_456_789
print(f"Tipe data a adalah {type(a)}")
print(f"Tipe data b adalah {type(b)}")
print(f"Tipe data c adalah {type(c)}")
print(f"Tipe data d adalah {type(d)}")

# Latihan Mengubah Tipe Data
two_digit_number = input("Masukkan dua digit angkat : ")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
str(two_digit_number)
print(int(two_digit_number[0]) + int(two_digit_number[1]))
# Data Types

# Operasi Matematika
print("\nOperasi Matematika")
a = 5+8
b = 10 - 5
c = 5*2
d = 10/2
e = 2**3
print(a)
print(b)
print(c)
print(d)
print(e)
# Operasi Matematika

# BMI Calculator
# 1st input: enter height in meters e.g: 1.65
print("\nBMI Calculator")
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
a = float(weight)
b = float(height)
bmi_calculation = a / b**2
print(int(bmi_calculation))

# Number Manipulation
# syntax round = round(angka_desimal, jumlah_angka_dibelakang koma)
print("\nNumber Manipulation")
print(round(2.6666666, 2))

# Life in Weeks
print("\n Life In Weeks")
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
hitung_minggu = (90 - int(age)) * 52
print(f"You have {hitung_minggu} weeks left.")

# String Format
fruit = "peaches"
weight = 3.0
per_pound = 2.99

output = "{1} are {2} per pound, and you have {0} pounds of {1}.".format(weight, fruit, per_pound)
print(output)