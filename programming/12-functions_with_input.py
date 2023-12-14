import math # math module for mathematical calculation

# Arguments and Parameters
my_name = "Govind"

def greet(name): # name is a parameter ( name of the data )
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