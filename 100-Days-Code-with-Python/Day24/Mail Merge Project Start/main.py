#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".\

PLACEHOLDER = "[name]"

starting_letter = "100-Days-Code-With-Python/100-Days-Code-with-Python/Day24/Mail Merge Project Start/Input/Letters/starting_letter.txt"
invited_names = "100-Days-Code-With-Python/100-Days-Code-with-Python/Day24/Mail Merge Project Start/Input/Names/invited_names.txt"

with open(starting_letter, "r") as file :
    starting_letter_content = file.read()

with open(invited_names, "r") as file :
    name_list = file.readlines()

for name in name_list :
    new_letter = starting_letter_content.replace(PLACEHOLDER, name.strip())
    with open(f"100-Days-Code-With-Python/100-Days-Code-with-Python/Day24/Mail Merge Project Start/Output/ReadyToSend/letter_{name.strip()}.txt", "w") as new_file :
        new_file.write(new_letter)
        print(f"Created letter for {name.strip()}")
        
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp