import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
nato_code = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic() :
  try :
    user_input = input("Please input a word: ").upper()
    phonetic_list = [nato_code[letter] for letter in user_input]
  except KeyError:
    print("Sorry, only letters in the alphabet please.")
    generate_phonetic()
  except KeyboardInterrupt :
    print("\nThank you...")
  else :
    print(phonetic_list)

generate_phonetic()