from art import logo,vs 
from game_data import data            
import os

def clear():  # function to clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[H\033[J')  # ANSI escape code to clear screen
    

import random

def compare(compareA,compareB):
  if compareA['follower_count'] > compareB['follower_count'] :
    return "A"
  elif compareA['follower_count'] == compareB['follower_count'] :
    return 0
  else:
    return "B"
  
def higher_or_lower():
  no_of_correct = 0 # define some varibles outside which are main and only restart/refresh when game restarts again and no need to put in while loops.
  game_on = True
  game_data = data  
  compareA = random.choice(game_data) # only once does it need to be random, other times it needs to be value of compareB and compareB gets new value. This will be a dictionary
  while game_on: # needed to get repeated user inputs 
    print(logo)
    if no_of_correct >= 1:
      print(f"You're right! Current score: {no_of_correct}.")
    compareB = random.choice(game_data)
    game_data.append(compareA) # adding again so doesnt give error when deleting again
    if compareA == compareB: # If both are same
        compareB = random.choice(game_data)
    print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}")
    print(vs)
    print(f"Compare B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}")
    user_input = input("Who has more followers? Type 'A' or 'B': \n").upper()
    if user_input == compare(compareA,compareB,user_input):
      no_of_correct += 1 
      clear()
      game_data.pop(game_data.index(compareA)) # checks if the dictionary is there in the list
      game_data.pop(game_data.index(compareB))
      compareA = compareB
    elif compare(compareA,compareB,user_input) == 0:
      compareA = compareB 
      no_of_correct += 1 
      clear()
    else:
      game_on = False 
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {no_of_correct}")
      

# Start Application
higher_or_lower()
    
    
    
  
  
