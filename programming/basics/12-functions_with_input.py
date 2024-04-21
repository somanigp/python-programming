import math # math module for mathematical calculation

# Arguments and Parameters
my_name = "Govind"

# : str,int,bool,float,list,tuple,dict,set,None,Custom_Class_Name - type of data as input if you wanna fix input
def greet(name: str): # name is a parameter ( name of the data )
  print(my_name) # we can access the variable defined outside the function as function and variable are in the same SCOPE.                
  print("Hello, " + name)

greet("John") # John - Arugment (actual data )

# Multiple Parameter 
def greet_with(name, location):
  print("Hello, " + name + " from " + location)

greet_with("John", "New York") # positional argument ( John - position of parameter and argument matches )
greet_with(location = "New York", name = "John") # keyword argument ( location = New York - position of parameter and argument are not relevant )

def paint_calc(height,width,cover):
  area = height*width
  no_of_cans = area/cover
  if no_of_cans > int(no_of_cans):
    no_of_cans = int(no_of_cans) + 1
  print(f"You'll need {int(no_of_cans)} cans of paint.")


num_cans = 4.3
round_up_cans = math.ceil(num_cans) # Return the ceiling of x as an Integral. if 4 then 4 , if 4.3 then 5
print(round_up_cans) # will print 5

def prime_checker(number):
  if (number <= 1):
    print("It's not a prime number.")
    return # exits the function without returning anything like we want in this case
  if number == 2 :
    print("It's a prime number.")
    return
  for i in range(2,int(number/2)+1): # Note : range(2,2)-> none as 2 should be also excluded as at right side
    if number % i == 0:
      print("It's not a prime number.")
      break # now wont execute else part also
  else: # loop fell through without finding a factor.In a for loop, the else clause is executed after the loop reaches its final iteration. And In a while loop, it’s executed after the loop’s condition becomes fals
    print("It's a prime number.")


# USE BOOLEANS - you dont need break or return
# def prime_checker(number):  
#   is_prime = True
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")  

def add1_remove2(list1: list): # functions can affect or alter lists
  list1.append(1)  # Only through list methods can we alter it , if we try to change it directly(affect attributes) it wont work.
  list1.remove(2)
  
l1 = [2]
add1_remove2(l1)
print(l1)

def change(ele):
    ele = [10]  # Assigning doesnt work but append,pop and other functions work.

x = [5]
change(x)
print(x)

# In Python, when you pass a list as an argument to a function, you're passing a reference to the list object. In the first example, `add1_remove2` modifies the contents of the list object referred to by `l1`, hence you see changes when you print `l1` outside the function.

# However, in the second example, `change` function reassigns the variable `ele` to a new list `[10]`, but this change does not affect the original list object referred to by `x`. This happens because reassigning `ele` creates a new reference to a different list object within the function's scope, leaving the original `x` unchanged.

# To modify the original list object directly inside the function, you would need to use methods like `append`, `pop`, etc., or use index-based assignment to change specific elements.
 
# NOTE: How to make sure only specific type of data is passed into a function
def only_int_input(only_int: int):  # Only takes int input
  return only_int+10

