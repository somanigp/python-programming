import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv('./nato_phonetic_alphabet.csv')
# print(type(data))  # DataFrame

dict_for_alphabets = {row.letter: row.code for (index, row) in data.iterrows()}  # Accessing different coln in a row
# print(dict_for_alphabets)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
output_list = [dict_for_alphabets[char.upper()] for char in input("Enter a word.\n")]
print(output_list)
