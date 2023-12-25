# Functions with o/p
def print_hello():
  return "Hello" # returns a string, replaces where the function was called.

x = print_hello() # assigns the return value to x
print(x) # prints x

def format_name(first_name, last_name): # Govind Somani - This is title case , first latter capital and the rest small
  if first_name == "" and last_name == "":
    return
  return first_name.title() + " " + last_name.title()

# Note:
print("Hi my name is Govind".title()) # Hi My Name Is Govind

x = format_name("GOVIND", "somani")
print(x)

# Multiple Return Statement 
# - once the function returns a value, it stops executing . It exits out of the function and other return statements are not exexcuted.

print(format_name(input("First Name : "), input("Last Name : "))) # prints None
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return 29
  else:
    return month_days[month-1] 

# Docstrings - Used to discribe a function , first line after declaration in a function
def area_of_square(side):
  """Returns the area of a square""""" # note for string its ''' '''
  return side * side

print(area_of_square.__doc__) # prints the docstring of the function

# You can define a function inside another function.
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)

# Calculator
def operation(num1,num2,to_do): # using dictionary with functions
  dict_calci = {
    "+": num1 + num2,
    "-": num1-num2,
    "*": num1*num2,
    "/": num1/num2
  }
  return dict_calci[to_do]

def calculator():
  to_calculate = True
  num1 = float(input("Whats the first number?\n"))
  while to_calculate:
    to_do = input("Pick an operation : +,-,* or / \n")
    num2 = float(input("Whats the second number?\n"))
    result = operation(num1,num2,to_do)
    print(f"The result is {result} .")
    to_continue = input(f"Do you wanna continue with {result}, type 'y' or type 'n' to quit or type 'new' for new calculation. \n").lower()
    if to_continue == "n": # if n is selected , it wont go to else part - no recursion will occur and while function and execution will end. 
      to_calculate = False
    elif to_continue == "y": # if y then while loop will continue and it won't call calculator function again , while loop will continue.
      num1 = result
    else:
      calculator() # recursion will occur and calculator function is called again. recursion - a function calling itself

# Start 
calculator()
    
# Notes : IMPORTANT
def add(n1,n2):
  return n1+n2
  
def subtract(n1,n2):
  return n1-n2

operations = {
  "+": add, # add function in a dictionary ***, function is passed an argument thus no parenthesis
  "-": subtract
}

function_is = operations["+"] # function is becomes 'add' funtion , thats why can take arguments

x = function_is(1,2)
print(x)

