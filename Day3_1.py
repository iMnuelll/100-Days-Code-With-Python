# Program Mengecek Tahun Kabisat
# Which year do you want to check?
year = int(input("Masukkan tahun : "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
decision1 = "Leap year"
decision2 = "Not leap year"

if year % 4 == 0 :
  if year % 100 != 0 :
    print(decision1)
  elif year % 100 == 0 :
    if year % 400 == 0 :
      print(decision1)
    else :
      print(decision2)
elif year % 4 != 0 :
  print(decision2)