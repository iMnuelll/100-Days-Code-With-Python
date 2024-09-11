import random

# # Random Intger
# random_integer = random.randint(1,100)
# print(random_integer)

# # Random Float
# random_float = random.random() * 5
# print(random_float)

# # Heads or Tails
# random_integer = random.randint(0,1)
# if random_integer == 1 :
#   print ("Heads")
# else :
#   print("Tails")

# # List
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# print(states_of_america)

# # Mengubah data yang berada di dalam list
# states_of_america[1] = "New Land"
# # Menambahkan data baru ke dalam list
# states_of_america.append("Old Land")

# print(f"\n{states_of_america}")\

# # Index Error
# num_of_states = len(states_of_america)
# print(states_of_america[num_of_states - 1])

# # Nested Lists
# fruits = ["Strawberies", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]
# print(f"\n{dirty_dozen[1][0]}")


# # Bank Roulette
# names_string = input("Masukkan nama-nama yang akan membayar? Pisahkan dengan koma\n")
# names = names_string.split(", ")

# # Mendapatkan total data yang ada di dalam list
# num_items = len(names)
# # Generate angka random dari list
# random_choice = random.randint(0, num_items - 1)
# # Choose and print a random name.
# print(names[random_choice])

# Treasure Map
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")