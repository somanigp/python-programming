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
a, b = b, a+b # cAN BE USED THIS WAY TOO 
a,b = b,a  # swap values
print(a)
print(b)