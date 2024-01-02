# How to write larger 'TODO'
# TODO: Create a letter using starting_letter.txt
#   for each name in invited_names.txt
#   Replace the [name] placeholder with the actual name.
#   Save the letters in the folder "ReadyToSend".
    
#   readlines() : This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#   replace() : This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#   strip() : THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# readlines() - method returns a list containing each line in the file as a list item.
PLACEHOLDER_FOR_NAME = "[name]"

list_of_names = []
with open("./Input/Names/invited_names.txt") as file:
    # list_of_names = file.readlines()  # Unlike if or while, its good to declare variable within 'with'
    for name in file.readlines():
        list_of_names.append(name.strip())  # removes '\n' in a string ('Govind\n') also

# print(list_of_names)

with open("./Input/Letters/starting_letter.txt") as file:
    content_of_letter = file.read()  # content_of_letter is a string

for name in list_of_names:
    # NOTE: use [name] as variables as they are easy to identify and replace.
    content = content_of_letter.replace(PLACEHOLDER_FOR_NAME, name)  # returns a string and doesnt make change in
    # official string.
    with open(f"./Output/ReadyToSend/letter_to_{name}", mode="w") as file:  # Path is also a string,
        # so we can create files with dynamic naming
        file.write(content)


# replace() - method replaces a specified phrase with another specified phrase.
# string.replace(old_value, new_value, count) #, by default, all occurrences get replaced

# strip() - removes any leading, and trailing whitespaces. Leading means at the beginning of the string,
# trailing means at the end.
# string.strip(characters) # characters - Optional. A set of characters to remove as leading/trailing characters

# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x) # banana
