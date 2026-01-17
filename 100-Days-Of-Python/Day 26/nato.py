# Loop through rows of a DataFrame
# dataframe = {new_key:new_value for (index, row) in dict.items()}
import pandas
import csv

# TODO: Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_dict)


# TODO: Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a Name: ").upper()
# print(user_input)

nato_code = [nato_dict[letter] for letter in user_input]
print(nato_code)