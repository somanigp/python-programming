# Hangman Game - Creating Flow Chart Helps

# Notes :
x = "abcd"
print('a' in x) # True - check if a letter exist in a string
l1 = list(x) # convert string to list
print(l1)
l2 = ["_"] * 5 # create list of "_" 5 times 
print('a' in l1) # search a element in a list 
for lett in x: # iterate over each char in a string 
    print(lett)

for _ in range(5): # Can use _ if not using the variable 
    print("Hi")

# Game Code
# import my_module_eleven # importing module which contains words & hangman
import random

no_of_chances = 6
print('Welcome to Hangman!')

# Selecting a Random Word 
from my_module_eleven import word_list, hangman # importing module which contains words & hangman. can also import like this -> no need to import whole module
random_word = random.choice(word_list)

# Creating Selected and Unselected list of the word
list_of_selected_word = list(random_word)
list_of_unselected_word = ["_"] * len(list_of_selected_word)  # easier way to create a list of same elements
print(list_of_unselected_word)
hangman_char = 0 # hangman figure

list_of_already_selected_letters = set() # Using Set as 'unique', iterable

while no_of_chances >= 0:
  # Taking letter as input from the user
  guessed_letter = input("Guess a letter: ").lower()
  
  if guessed_letter in list_of_already_selected_letters: # If user already did this input 
      print("You have already selected this letter. Please try again.")
  elif guessed_letter in list_of_selected_word:
    list_of_already_selected_letters.add(guessed_letter)  # add element in a set
    # Replacing the underscore with the letter everywhere 
    for i in range(len(list_of_selected_word)):
      if list_of_selected_word[i] == guessed_letter:
        list_of_unselected_word[i] = guessed_letter
    print('Correct Guess!!')
    print(list_of_unselected_word)
    if "_" not in list_of_unselected_word: # opposite of 'in' is 'not in'
      break # Will take out of while loop 
  else:
    list_of_already_selected_letters.add(guessed_letter)  # add element in a set
    no_of_chances -= 1
    print(hangman[hangman_char]) # using imports
    hangman_char += 1
    if no_of_chances >= 0:
      print("Wrong guess! You have", no_of_chances, "chances left.")
  # printing the remaining list 
    print(list_of_unselected_word)

# Checking if the user has won or not
if list_of_unselected_word == list_of_selected_word:
  print("Congratulations! You have won the game.")
else:
  print("You have lost the game.")