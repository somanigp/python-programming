# loops and data-structures
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# https://docs.python.org/3/tutorial/controlflow.html#for-statements

# Strings
print("STRINGS AND INTS")
abc = " abc "
print("##" +abc.strip()+"##") # removes extra space and new line
del abc # to delete an entire variable

#int
print(abs(-9)) 
print(abs(-9.55))

# Lists
print()
print("LISTS")
from collections import deque # Imprting just a method
queue = deque(["Eric", "John", "Michael"]) # Queues - FIFO
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
print(queue)                    # Remaining queue in order of arrival


# NOTE: 
# list.pop() -> removes last element
# list.pop(index) -> removes element at index

l3 = [1,2,3,4,5,6,7,8,9]
del l3[:4] # use del with list to delete elements . [5, 6, 7, 8, 9]
# print(l3)
del l3[:] # delete complete list
# print(l3)

l1 = [1,3,53,63,3,9]
del l1[1] # deletes the item at index 1
sorted(l1) # doesnt alter the original list 
l1.sort() # Alters the original list
print(l1)

l4 = l1.copy() # copies the list, doesnt affect the original list 
l4.append(99)
print(l1,l4) # can print 2 list side by side

# List Comprehension
# squares = []
# for x in range(10):
#     squares.append(x**2) # can you like this
# print(squares)

squares_through_comprehension = [x**2 for x in range(10)]

# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))

combs_through_comprehension = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] # create list of tuples
print(combs_through_comprehension)

vec = [-4, -2, 0, 2, 4]
list_1 = [x for x in vec if x >= 0] # if to make list 

# Tuples - are immutable and ordered
# NOTE: Slicing works for tuples and lists and all other orders class like strings.
# So we can slice a tuple to get a part of it.
print()
print("TUPLES")
t = 12345, 54321, 'hello!' # can define tuples like this
t2 = (1,2,3,4,5) # or this
print(t[0],t)  # Tuples are ordered , accessed thorugh index

list_is = [1,2,3,4,5]
tuple_is = tuple(list_is) # convert list to tuple

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u2 = (t, (1, 2, 3, 4, 5))
print(u)

# Tuples are immutable:
# t[0] = 88888 # will give error

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])

empty = () # empyt tuple
singleton = ('hello',)    # single value tuple <-- note trailing comma
len(empty)
len(singleton)
print(singleton)

t5 = (12345, 54321, 'hello!') # tuple packing
x, y, z = t5 # tuple unpacking  

l1 = [(1,2,3),(4,5,6)]
for x,y,z in l1:
  print(x,y,z)
  

# Sets  - unordered meaning position doesnt matter,unique, iterable
print()
print("Sets".upper())
aSet = set() # an empty set 
print(type(aSet))
aSet = {1,2,3,4,5,6,7,8,9} # set of integers
print(aSet)

# Create a set
my_set = {1, 2, 3, 4, 5}

# Remove an item using remove()
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5}

# Remove an item using discard()
my_set.discard(5)
print(my_set)  # Output: {1, 2, 4}

# Create a set
my_set = {1, 2, 3, 4, 5}

# Add an item using add()
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Set Comprehension
a = set('abracadabra') # create a set(unique letters) from a string 
b = set('alacazam')
print(a)                             # unique letters in a
print(b)
print(a - b)                         # letters in a but not in b
print(a | b)                         # letters in a or b or both
print(a & b)                         # letters in both a and b
print(a ^ b)                         # letters in a or b but not both
a = {x for x in 'abracadabra' if x not in 'abc'} # For dict we put {x:x**2 for x in range(1,11)} , we use x:x**2
# NOTE: 
a = {1,2,3,4,7}
b = {1,2,3,4,5}
print(b-a) # {5}
print(a^b) # {5,7}

a = [x for x in 'abracadabra' if x not in 'abc'] # this will give list
print(a)

print('a' in 'abc') # True
print('ab' in 'abc') # True NOTE**
print('a' in ['a','b']) # True

# Dictionary - unordered
print()
print("Dictionary".upper())
users = {'Hans': 'inactive', 'govind': 'active', 'raksha': 'active'} 
# print(type(users))
print(users.keys())

# Strategy:  Iterate over a copy
# .items() - returns a list of tuples(key, value)
# .keys() - returns a list of keys
# .values() - returns a list of values
for user, status in users.copy().items(): # iterate over k,v pairs at once, this also alters the original dictionary
    if status == 'inactive':
        users.pop(user) # delete items in a dictionary

print(users)

# Strategy:  Create a new collection
active_users = {} # initialize dicts
for user, status in users.items():
    if status == 'active':
        active_users[user] = status # add items in dictionary 

# Convert Dict to list
l2 = list(active_users)
print(l2) # removes values and keep only keys 

dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) # converting a list of tuples to a dictionary
print(dict1)
dict3 = dict(sape=4139, guido=4127, jack=4098) 
#dict comprehension
dict2 = {x: x**2 for x in range(1, 11)}
print(dict2)

# zip - combines iterables
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    
## Loops Keywords:

print(sum(range(4))) # range provides a list to work with 
      
# The break statement breaks out of the innermost enclosing for or while loop.
for i in range(3):
  for j in range(1):
    if i == 1:
      break # gets out of the j loop and not i loop
    print(i)
    
# continue statement jumps to the next iteration of the loop
for i in range(3):
  for j in range(1):
    if i == 1:
      continue # skips the j loop and not i loop
    print(i)
    
# pass statement is used to skip a statement
class MyEmptyClass:
  pass

while False:  
  pass

# else statement is used to execute code when the condition is false
# In a for loop, the else clause is executed after the loop reaches its final iteration.
# In a while loop, it’s executed after the loop’s condition becomes false.
for n in range(2, 10):
  for x in range(2, n):
      if n % x == 0:
          print(n, 'equals', x, '*', n//x)
          break # if break is there it doesnt go to else part
  else:
      # loop fell through without finding a factor
      print(n, 'is a prime number')

# Match : introduced in python 3.10

def http_error(status):
  match status:
    case 401 | 403 | 404:
      return "Not allowed"
    case 404:
      return "Not found"
    case 418:
      return "I'm a teapot"
    case _:
      return "Something's wrong with the internet"

# match point:
# case (0, 0):
#     print("Origin")
# case (0, y):
#     print(f"Y={y}")
# case (x, 0):
#     print(f"X={x}")
# case (x, y):
#     print(f"X={x}, Y={y}")
# case _:
#     raise ValueError("Not a point")