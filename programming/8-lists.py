# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists


#list  - data structure , single piece of data - variable . This is one way of saving or organizing data. to store a group of same data in a proper order.

l1 = [1,2,"a", "b", "c", True]
#print(l1[100]) - IndexError : list index out of range
print(l1)
print(type(l1))

print(l1[0]) # access element of a list 
print(l1[-1]) # access last element of a list
print(l1[1:3]) # access a range of elements of a list
print(l1[1:5:2]) # access a range of elements of a list, but every second element 
print(l1[::-1]) # reverse a list 

l1[0] = 3 # change element of a list 
print(l1)
l1.append("d") # add element to the end of a list 
print(l1)
l1.insert(3, "e") # add element to the 3rd position of a list , the rest of elements will be shifted to the right 
print(l1)

x = l1.pop(1) # remove element from that index from the list 
print(x)
print(l1)

l1.clear() # remove all elements from a list 
print(l1) # [] 

# making a list out of string : 
names_string = "John,Mary,Bob,Alice"
names = names_string.split(",")
print(names)

names = names_string.split(", ")
import random 
length_of_names = len(names)
random_person_index = random.randint(0,length_of_names-1) # -1 because index starts from 0
print(f"{names[random_person_index]} is going to buy the meal today!")

#nested lists
odd = [1,3,5]
even = [0,2,4]

l1 =[odd,even]
print(l1)
print(l1[0][1]) #x,y 
l1[0][0] = 10
print(odd) # original list also changes , ie odd list changes


##############

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()
x_axis = position[1]
y_axis = position[0].upper()

if y_axis == "A":
  y = 0
elif y_axis == "B":
  y = 1
else:
  y = 2

map[int(x_axis)-1][y] = "X"

print(f"{line1}\n{line2}\n{line3}") # line1,line2,line3 changes 

abc = ["a", "b", "c"]
letter_index = abc.index("a") # gives 0 - index of a