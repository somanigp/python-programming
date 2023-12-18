################### Scope ####################

enemies = 1
# NOTE : While and for loops can alter 'enemies' (as enimies is outside those loops) as they are in the same scope. But functions cant. Also if something in defined in a loop , it cant be used outside the loop.

def increase_enemies():
  enemies = 2 # this is newly declared variable and declared inside this function. And has a scope limied to this function. This variable is not the variable 'enemies' in the main scope.
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope - Variables declared inside a function are local to that function.

def hello():
  name = "John"
  print(f"Hello {name}")

hello()
# print(name) # name cant be accessed here # name is not defined in this scope. ** NOTE ** 

# Global Scope - Variables declared outside a function are global to that file.
x = 10

def hello_func():
  print("Inside hello " , x) # x is global to this file. x can be accessed here but not altered in this function.
  # x = 5 - this will create a new variable x in this function which can be accessed only in this function.

hello_func()
print(x)

# Anything that we define/create (functions,variables,etc ) has a namespace and that namespace has a scope/limit. 


# NOTE 
def x1():
  def x2():
    print("Hello x2")
  x2() # can only be accessed inside in this scope.

# x2() # x2 is not defined in this scope. Cant be accessed here


# NOTE : NO block scope in python (if, for, while, etc)
# A variable created within a function is only accessable within that function.

x=10
if x<20: # there is no block scope in python , if some variable created in 'if', 'while' or for loop  statement then it is accessable across , as it is also global.
  
  new_variable =10 # NOTE : Has same scope as enclosing function and if no enclosing function then it is global.

print(new_variable) # new_variable is accessable here

x = 10
while x < 11:
  new_value = 10
  x+=1

print(new_value)

for i in range(5):
  i = 10

print(i)

# MOdifying global scope
# Dont use same name for local and global variables 

enemies = 1
#******# NOTE 
def increase_enemies():
  global enemies # tells that there is a global variable called 'enemies' defined somewhere outside this function and to access that .
  enemies += 1  # this is the enimies defined globally.
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# NOTE : Never try to modify global variables inside a function, you can use it but dont modify. 

x1 = 1

def x3():
  print(x1) # can print it 
  # x1 += 2 - will give error 
  return x1 + 1 # if global variables used directly in return statement then it works. As its not altering the value of x1 but just using x1

print(x3())

# GLOBAL CONSTANTS - define globally and never change

PI = 3.14 # All uppercase for global constants so to differentiate from others. These variables dont change value within function. 
URL  = "https://www.google.com"


def circumference(radius):
  return 2 * PI * radius


# NOTE 

ini = 1

def new_func():
    ini = 5
    return ini # will return local variable 

new_func()
print(ini) # will print 1

## GUESSING GAME ##

# Logo Link: Create your own logo
# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Guess%20The%20Number 

logo = '''


  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       

'''
import random 

print(logo)
print("Welcome to the Number Guessing Game!")

def guessing_game():
  has_won = False
  no_of_attempts = 10 
  selected_number = random.randint(1,100)
  print("I'm thinking of a number between 1 and 100.")
  mode_selected = input("Choose a difficulty. Type 'easy' or 'hard ?\n").lower()
  
  if mode_selected == "hard":
    no_of_attempts = 5
  
  while no_of_attempts > 0 and not has_won:
    print(f"You have {no_of_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess. \n"))
    if guess > selected_number:
      print("Too High !")
      no_of_attempts -= 1
    elif guess < selected_number:
      print("Too Low !")
      no_of_attempts -= 1
    else:
      print("You Winnn !!")
      has_won = True
  
  if not has_won:
    print("You Lose !!")
  
  if input("Wanna Try Again ? y or n \n").lower() == "y":
    guessing_game()

# Starting Game
guessing_game()


  
