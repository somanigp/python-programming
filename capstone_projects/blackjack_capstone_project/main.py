############### Blackjack Project #####################

import random
import os

def clear():  # function to clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[H\033[J')  # ANSI escape code to clear scree

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def add(l):
  """Add all elements in a list."""
  result = 0
  for i in l:
    result += i
  return result
  #return sum(l) - sum function adds all elements in a list

def deal_card():
    """Returns a new card."""
    return random.choice(cards)

def compare(users_card,computers_card):
  """ Compares users_card and computers_card and tells the winner ."""
  if add(users_card)>21:
    print("Your cards : ",users_card," your total is : " ,add(users_card))
    print("Computer cards : ",computers_card," computer total is : " ,add(computers_card))
    print("You Lose")
  elif add(computers_card)>21:
    print("Your cards : ",users_card," your total is : " ,add(users_card))
    print("Computer cards : ",computers_card," computer total is : " ,add(computers_card))
    print("You Win !!")
  # normal checking who has greater card
  else:
    print("Your cards : ",users_card," your total is : " ,add(users_card))
    print("Computer cards : ",computers_card," computer total is : " ,add(computers_card))
    if add(computers_card) > add(users_card):
      print("computer wins, sorry ")
    elif add(computers_card) == add(users_card):
      print("Its a draw!")
    else:
      print("you win !!")

def play_again():
  if input("Wanna play a new game? y or n : ") == "y":
    blackjack()
  else:
    print("thank you!")

def blackjack():
  clear()
  users_card = [deal_card(),deal_card()] # directly calling functions which return integers in a list
  # if users gets dealed 11 , 11
  if add(users_card) == 22:
    users_card = [1,1]
  
  computers_card = [deal_card(),deal_card()]
  # if computer gets dealed 11 , 11
  if add(computers_card) == 22:
    users_card = [1,1]

  # print initial cards
  print("Your cards : ",users_card," your total is : " ,add(users_card))
  print("Computer cards : ",computers_card[0]," computer total is : " ,add(computers_card[:1]))
  
  # if anyone has blackjack - happens only when no. of cards is 2
  if (add(computers_card) == 21) or (add(users_card) == 21):
    compare(users_card,computers_card)
    play_again()
    return # needed here as after the blackjack inside play_again is completed , this blackjack function shouldnt execute further
  
  to_pick_another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
  if to_pick_another == "y":
    # Picking players card
    while add(users_card)<=21:
      card = deal_card()
      if card == 11 and ((card + add(users_card)) > 21):
        if 11 in users_card:
          index = users_card.index(11)
          users_card[index] = 1
        card = 1
      elif (11 in users_card) and (card + add(users_card)>21):
        index = users_card.index(11)
        users_card[index] = 1
      users_card.append(deal_card())
      print("Your cards : ",users_card," your total is : " ,add(users_card))
      print("Computer cards : ",computers_card[0]," computer total is : " ,add(computers_card[:1]))
      if add(users_card)>21:
        break
      if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "n":
        break
    # picking computers card 
    while add(computers_card) <= 17:
      card = deal_card()
      if card == 11 and ((card + add(computers_card)) > 21):
        if 11 in computers_card:
          index = computers_card.index(11)
          computers_card[index] = 1
        card = 1
      elif (11 in computers_card) and (card + add(computers_card)>21):
        index = computers_card.index(11)
        computers_card[index] = 1
      computers_card.append(deal_card())
    clear()
    # compare
    compare(users_card,computers_card)
    # wanna play again
    play_again()
    
  else:
    # getting rest of computers cards
    while add(computers_card) <= 17:
      card = deal_card()
      if card == 11 and ((card + add(computers_card)) > 21):
        if 11 in computers_card:
          index = computers_card.index(11)
          computers_card[index] = 1
        card = 1
      elif (11 in computers_card) and (card + add(computers_card)>21):
        index = computers_card.index(11)
        computers_card[index] = 1
      computers_card.append(deal_card())
    # compare 
    compare(users_card,computers_card)
    # wanna play again
    play_again()

# Start Application
if input("Do you wanna play blackjack? y or n :").lower() == "y":
  blackjack()
else:
  print("Thank you!!")

  
