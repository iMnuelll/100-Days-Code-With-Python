# For Loop with List
# Guet user answer
#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_choice = random.choice(word_list)
print(random_choice)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
ask_user = input("Guess a letter : ")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in random_choice :
    if ask_user == i :
        print("Right")
    else :
        print("Wrong")