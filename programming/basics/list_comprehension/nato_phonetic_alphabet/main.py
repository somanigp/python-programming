import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv('./nato_phonetic_alphabet.csv')
# print(type(data))  # DataFrame

dict_for_alphabets = {row.letter: row.code for (index, row) in data.iterrows()}  # Accessing different column in a row
# print(dict_for_alphabets)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# is_on = True
# while is_on:
#     try:
#         output_list = [dict_for_alphabets[char.upper()] for char in input("Enter a word.\n")]
#     except KeyError:
#         print("Sorry only letters in the alphabet please")
#     else:
#         print(output_list)
#         break


def generate_dict() -> None:
    try:
        output_list = [dict_for_alphabets[char.upper()] for char in input("Enter a word.\n")]
    except KeyError:
        print("Sorry only letters in the alphabet please")
        generate_dict()  # When face error then trigger the function again. - Recursion** use case
    else:
        print(output_list)
