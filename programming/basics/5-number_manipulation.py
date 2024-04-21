print(8/3) # print float number 
print(int(8/3)) # print integer part of it
print(round(8/3)) # round into integer 
print(round(8/3,2)) # upto 2 decimal points

x = 10
x+= 2 # x = x + 2
print(x)
x-= 2
print(x)
x*= 2
print(x)
x/= 2
print(x)

#f-string
name = "Saurabh"
age = 20
is_below_18 = False
print(f"My name is {name} and my age is {age} and I am below 18 : {is_below_18}")

print(round(5 / 2, 2))  # 2.5
print("{:.2f}".format(5 / 2)) # 2.50 
# .2f stands for "floating-point number with two decimal places"
# uses a colon to specify that the floating-point number should be formatted with two decimal places.