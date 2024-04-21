# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# Functions: append, extend, insert, remove, pop, clear, index, count, sort, reverse
# l1[0] = 3
# l1.append("d")
# l1.insert(3, "e")
# l1 += l2
# x = l1.pop(1) 
# names = names_string.split(",")
# l1.clear()
# letter_index = abc.index("a")
# list.remove(ele) - remove first occurence of that element
# student_scores.sort() -> acsending order(small to big)
# student_scores.sort(reverse=True) -> desending order(big to small)
# maximum = max(numbers) # max and min for a list of numbers 

#list  - data structure , single piece of data - variable . This is one way of saving or organizing data. to store a group of same data in a proper order.

l1 = [1,2,"a", "b", "c", True]
#print(l1[100]) - IndexError : list index out of range
print(l1)  
print(type(l1))  # list 

print(l1[0]) # access element of a list 
print(l1[-1]) # access last element of a list
print(l1[1:3]) # access a range of elements of a list
print(l1[1:5:2]) # access a range of elements of a list, but every second element 
print(l1[::-1]) # reverse a list 

l1[0] = 3 # change element of a list on that index
print(l1)
# add element to a list 
l = []
l += "1" # only with strings , this is equivalent to extend 
l += "2"
print(l) 

l = []
l10 = [11]
l += l10 # += is extends which adds 2 lists

l1.append("d") # add element to the end of a list 
print(l1)
l1.insert(3, "e") # add element to the 3rd position of a list , the rest of elements will be shifted to the right 
print(l1)

x = l1.pop(1) # remove element from that index from the list 
print(x)
print(l1)

# list.remove(ele) - remove first occurence of that element

l1.clear() # remove all elements from a list 
print(l1) # [] 

# making a list out of string : 
names_string = "John,Mary,Bob,Alice"
names = names_string.split(",")
print(names)

names = names_string.split(", ") # ['John,Mary,Bob,Alice']
print(names)
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