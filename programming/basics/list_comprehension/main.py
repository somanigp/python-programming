# List Comprehension is a case where you create a new list from an existing list/sequence
# Sequences are: list, range, string, tuple
# new_list = [ new_item for item in list_a ]
import random

list_a = [1, 2, 3]
list_b = [x+1 for x in list_a]
print(list_b)

name = "Govind"
list_b = [char for char in name]
print(list_b)

list_b = [i*2 for i in range(1, 11)]
print(list_b)

# Conditional List Comprehension:
# new_list = [ new_item for item in list_a if test]
list_b = [num for num in list_a if num > 2]
print(list_b)

names = ['Cat', 'Rat', 'Mat', 'robert', 'govind']
names = [n.title() for n in names if len(n) > 3]  # Will use the above list and store it in the same variable.
# print(n) will print Govind
print(names)

input_in_strings = "1, 2, 3, 4, 5, 6"
list_of_strings = input_in_strings.split(',')
print(list_of_strings)  # ['1', ' 2', ' 3', ' 4', ' 5', ' 6'] - they contain white spaces still
list_of_int = [int(num) for num in list_of_strings]
print(list_of_int)  # [1, 2, 3, 4, 5, 6] - ' 6' will also be converted to int

file_1 = [1, 5, 8, 234, 235, 65, 70]
file_2 = [1, 5, 8]
result = [x for x in file_1 if x in file_2]  # To find common values in 2 list without O(n**2), or double for loop.
print(result)

# NOTE: ** for converting to int we don't need to strip white spaces
a = "12\n"
b = int(a)
print(b)

# Dictionary Comprehension: Create new dictionary from the values in a list/dictionary/sequence
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}
names = ['Cat', 'Rat', 'Mat', 'robert', 'govind']
random_scores = {name: random.randint(1, 100) for name in names}
print(random_scores)
passed_students = {name: score for (name, score) in random_scores.items() if score > 60}
# for (name, score) in random_scores.items():  # Equivalent of above expression
#     if score > 60:
#         passed_students[name] = score
print(passed_students)  # Note it will only take the name for which the corresponding value is over 60.
# As it will go into if only for names which have score > 60, thus only those names will be added.

# Pandas: you can loop through the same way as you working with python dictionary of below structure
students = {
    "names": ["Govind", "Raksha", "Yash"],
    "scores": [99, 40, 50]
}
import pandas

student_df = pandas.DataFrame(students)
# print(student_df)

# for (k, v) in student_df.items():  # iterate through columns
#     # print(k)
#     print(v)

# Pandas: How to iterate through each of the rows in a df
for (index, row) in student_df.iterrows():
    print(index)
    print(row.names)  # Can access each of the values in a row
