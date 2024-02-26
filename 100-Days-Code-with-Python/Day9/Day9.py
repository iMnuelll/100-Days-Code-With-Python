programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# Print the dictionary
print(f"This is the dictionary {programming_dictionary}\n")

# Print one of the values in the dictionary
print(f"Print one of the values in the dictionary : {programming_dictionary["Bug"]}\n")

# Remove one of the values from the dictionary
del programming_dictionary["Bug"]
print(f"After remove one of the value in dictionary {programming_dictionary}\n")

# Add a new value to the dictionary
programming_dictionary["Bug"] = "An error in a program that prevents the program from running as expected"
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(f"After add other value to the dictionary {programming_dictionary}\n")

# Using for loop to print the dictionary
for key in programming_dictionary :
    # Print the key and value
    print(f"{key} : {programming_dictionary[key]}")

# Nesting a list in dictionary
travel_blog = {"France": ["Paris", "Lille", "Dijon"],
               "Indonesia" : ["Jakarta", "Bandung", "Medan"]
               }
print(f"\nThis is nesting a list in dictionary :\n{travel_blog['France']}")

# Nesting a dictionary in dictionary
travel_blog = {"France": {"Cities visited" : ["Paris", "Lille", "Dijon"]},
               "Indonesia" : {"Cites visited" : ["Jakarta", "Bandung", "Medan"]}
               }
print(f"\nThis is nesting a dictionary in dictionary :\n{travel_blog['France']}")

# Nesting a dictionary in a list
travel_blog = [
    {
     "Country" : "France", 
     "Cities visited" : ["Paris", "Lille", "Dijon"]
     },
     {
      "Country" : "Indonesia", 
      "Cites visited" : ["Jakarta", "Bandung", "Medan"]
      }
]
print(f'\nI have been visited {travel_blog[0]['Country']}, and my favorites place is {travel_blog[0]['Cities visited'][0]}')