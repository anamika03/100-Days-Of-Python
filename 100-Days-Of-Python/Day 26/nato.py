# Loop through rows of a DataFrame
# dataframe = {new_key:new_value for (index, row) in dict.items()}
import pandas
import csv

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_input = input("Enter a Name: ").upper()
    try:
        nato_code = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Please enter a valid name containing only letters.")
        generate_phonetic()
    else:
        print(nato_code)
        print("\n")

generate_phonetic()

