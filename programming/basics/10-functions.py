# Functions : built in and custom(ours) function

#Syntax  
def my_function():
  print("Hello World") # indentaion 

# Calling the function
my_function() # define before calling or else error

# Parameters and Arguments
def my_function(name):
  print("Hello my man " + name) # indentaion

# Calling the function
my_function("John") 

# return value
def my_function(x) -> str: # return type is str # scope of x is only within the function
  return "Hello " + x

# Calling the function
x = my_function("John") # it will take the latest definition of my_function
print(x)

# ** all three functions have the same name like variables , the one recently defined will be used

# Code Blocks - Through identation 
# A variable defined in a block will only be available in that block - if you try to use it outside the block it will throw an error. Known as "scope"

 # Indentation : 4 spaces / tab but not both in a file, from python 3

# indend setting -> set to spaces and four -> when u do tab 

# While loops : While loops are used to repeat a block of code as long as a condition is true.

# Syntax : 
# while condition:
#   block of code
#   increment/decrement/break

x = 1
while x<4:
  print(x)
  x = x + 1 # So doesnt go into infinite loop

# for - to iterate and do something with each item in a list
# while - until some condition is met

