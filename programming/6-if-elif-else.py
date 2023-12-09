num = 5
if num<10: #if it goes into the first if statement, it will not go into the second if/elif statement
  print("small")
elif num<20:
  print("medium")
else:
  print("large")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height < 120:
    print("Sorry, you are too short to ride this rollercoaster.")
else:
    print("Enjoy the ride!")
    age = int(input("What is your age? "))
    if age < 12:
      bill = 5
      print("Please pay $5")
    elif age > 18:
      bill = 12
      print("Please pay $12")
    else:
      bill = 7
      print("Please pay $7")
    wants_photo = input("Do you want a photo taken? Y or N ")
    if wants_photo.upper() == "Y":
      bill+= 3
    print(f"YOur final bill is ${bill}")

x = 20
if x > 10:
    print("x is greater than 10")
elif x < 5:
    print("x is less than 5")
else:
    print("x is between 5 and 10")

# = -> assigning a value , == -> comparing two values
# if x == y -> x is equal to y
# if x != y -> x is not equal to y
# if x > y -> x is greater than y
# if x < y -> x is less than y
# if x >= y -> x is greater than or equal to y
# if x <= y -> x is less than or equal to y

height = float(input())
weight = int(input())
bmi = weight/(height**2)
if bmi<18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi<25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi<30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi<35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
  
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 ==0:
      print("Leap year")
    else:
      print("Not leap year")
  else :
    print("Leap year")
else:
  print("Not leap year")
  
  
# if one condition is met then the other statements elif and else will not be executed :
# if age < 12:
#     print("Please pay $5")
# elif age > 18:
#     print("Please pay $12")
# else:
#     print("Please pay $7")

# if there are multiple if statements one after the other then they will be executed :
# if age < 12:
#     print("Please pay $5")
# if age > 18: - it will check this also evenif the above condition is met
#     print("Please pay $12")


# Lgical Operators : and , or , not
if True and False:
    print("True and False")
if True or False:
    print("True or False")
if not True: # reverses a condition
    print("not True")
if not False:
    print("not False")
    
str1 = "abababadsidjei"
print(str1.count("a")) # no of chars in the string 
print(str1.count("a", 1, 5)) # no of chars in the string from index 1 to 5
print("SPD".lower()) # prints the lower case of the string