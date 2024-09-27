import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
nato_code = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please input a word: ").upper()
phonetic_list = [nato_code[letter] for letter in user_input if letter in nato_code]

print(phonetic_list)