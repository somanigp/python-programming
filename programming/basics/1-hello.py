# Python Documentaion = https://docs.python.org/3/tutorial/interpreter.html

print("Hi"); print("Hi") # This is valid and NOTE: print has a newline at the end so 2nd Hi will be in the next line 
print("Hello, World! \n") # \n is an escape sequence that inserts a newline 
# "Hello, World!" is a string literal
print("Hello World\nHello World")
print("Hello " + "Govind")
# start with no intend in code. 
print('String Concatenation is done with the "+" sign.') # can alternate between single and double quotes for strings
input("What is your name?")# prompts user to input a value just after showing this prompt ie no newline . Also the value coming in replaces this.
input("What do you love?\n")
print("Hello " + input("What is your name?\n")) #Thonny IDE for stepover -> it means it goes to hello and then process input , gets input value and then concatenate whole string and then returns the final string.
# note after taking the input it creates a newline .
x = int(input())
y = int(input())
#input will look as below :
#2
#3
print(x + y)
# name = input("What is your name?\n") # defining a variable 
print(len(input("What is your name?\n"))) # length of the string  

print('''
      Can write anything in between as much as you want.
      In multiple lines.
      ''')
print('Aren\'t you a little short for a storm trooper?') # backslash before ' or " , tells to ignore that one and its part of string 
print("What is a \"chopper\" \t?") # use \t for tab
