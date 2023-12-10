# https://docs.python.org/3/tutorial/controlflow.html#for-statements

#loops - repeating code
#while loops - repeating code until a condition is false
#for loops - repeating code a set number of times
#range - a sequence of numbers

fruits = ["apple", "banana", "cherry"]
for fruit in fruits: # go through each item in a list 
  print(fruit) # fruit - name of a single item

# Input a Python list of student heights
student_heights = input("Give heigths").split() # input is like and by default it split by place :123 128 981 251 
for n in range(0, len(student_heights)): # range(a,b) -> b in not included
  student_heights[n] = int(student_heights[n]) # convert to int
total_heigth = 0
for heigth in student_heights:
  total_heigth += heigth
print(f"total height = {total_heigth}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(total_heigth/len(student_heights))}")

# student_scores.sort() -> acsending order(small to big)

# student_scores.sort(reverse=True) -> desending order(small to big)

student_scores = input("Give Scores").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_number = 0 
for score in student_scores:
  if score > highest_number:
    highest_number = score 

print(f"The highest score in the class is: {highest_number}")

numbers = [10, 7, 25, 14, 30]
maximum = max(numbers) # max and min for a list of numbers 

for num in range(10): # exclude 10
    print(num)
for num in range(1,10): # excludes 10 
  print(num)

for num in range(1,11,3): # step by 3 - 1 4 7 10
  print(num)

for num in range(10,1): # will not print anything 
  print(num)

for num in range(10,0,-1): # reverse order, excludes 0
  print(num)

target = int(input("Give a target")) 
even_sum = 0
for number in range(2, target + 1, 2): # calculates even number directly
  even_sum += number
print(even_sum)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n")) # can use f-string in input as well
nr_numbers = int(input(f"How many numbers would you like?\n"))

list_of_letters = random.choices(letters, k=nr_letters) # Return a k sized list of population elements chosen with replacement.
list_of_numbers = random.choices(numbers, k=nr_numbers)
list_of_symbols = []
for i in range(nr_symbols):
    list_of_symbols.append(random.choice(symbols))
lv1password_list = list_of_letters + list_of_symbols + list_of_numbers # concat list 
lv1password = "".join(lv1password_list) # join list to string
print(lv1password)

random.shuffle(lv1password_list) # shuffle list
lv2pasword = "".join(lv1password_list) # join list to string
print(lv2pasword)