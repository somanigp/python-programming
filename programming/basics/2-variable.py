from typing import Final

name = input("What is your name?")
print(f"Hello {name}") #Using formatter 
print("Hello" + name) #Using concatenation
print("Hello", name, "!") #Using concatenation and comma
name = "Vyankatesh" 
print(name)
lenght = len(name)
print(lenght) # directly print variables 

x = "String"
x = 2 # x can be of any type
print(x)
print(type(x)) # print the type of x

# Variables can be defined in this way also :
a , b = 1 ,2 
a, b = b+10,a # Both get assigned in a same go. ** so a = b + 10 doesnt happen first
print(a, b)
a, b = b, a+b # cAN BE USED THIS WAY TOO 
a,b = b,a  # swap values
print(a)
print(b)

str1: str = "Hello"
str1 = "hello agina"
print(str1)
str1 = 2 # Allowed 
print(type(str1)) # int type

str2: Final[str] = "Hello"
print(str2)