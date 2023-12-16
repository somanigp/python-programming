import os

def clear_screen():  # function to clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[H\033[J')  # ANSI escape code to clear screen
    

programming_dictionary = {
    "Bug":
    "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Get key from Value 

my_dict = {'a': 10, 'b': 30, 'c': 20}

max_key = max(my_dict, key=my_dict.get) # One approach involves using the max() function with a custom key argument to retrieve the key corresponding to the maximum value.  The key argument specifies a function to be called on each element before comparison. 'my_dict.get' is a function that retrieves the value for each key in the dictionary.
max_value = my_dict[max_key]

# print(f"The key '{max_key}' has the highest value of {max_value}.")

def get_key_from_value(dictionary, search_value):
  for key, value in dictionary.items():
      if value == search_value:
          return key
  return None  # If the value is not found in the dictionary

# Dict - unordered meaning position doesnt matter 

programming_dictionary = {
    "Bug":
    "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# retrieve a data from a dictionary
print(programming_dictionary["Bug"])

# add a new key-value pair to a dictionary
programming_dictionary["Loop"] = "A block of code that is repeated."

# print the dictionary
# print(programming_dictionary)

# edit an item in a dictionary
programming_dictionary["Loop"] = "A block of code that is repeated until a condition is met."
# print(programming_dictionary)

# remove an item from a dictionary
programming_dictionary.pop("Bug")
# print(programming_dictionary)

# Lopp through a dict 
for key in programming_dictionary: # only shows/loop through keys 
    print(key)

# create an empy dictionary
empty_dictionary = {}

# Wipe an entire dictonary
programming_dictionary = {}
# print(programming_dictionary)

# del whole dict
del programming_dictionary



# Always start with highest in if-elif-else , as when it goes through one, it doesnt go into others
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

for key in student_scores: # access keys in a dict
  if student_scores[key] > 90: #91-100
    student_grades[key] = "Outstanding"
  elif student_scores[key] > 80: #81-90
    student_grades[key] = "Exceeds Expectations"
  elif student_scores[key] > 70: #71-80
    student_grades[key] = "Acceptable"
  else: # <=70
    student_grades[key] = "Fail"
    

#########################################

## NESTING

#list inside dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
  "Italy": ["Rome", "Venice", "Florence"]
}

#Dictionary in a dictionary - actual data is like this
complex_travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
  },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
  },
  "Italy": {
    "cities_visited": ["Rome", "Venice", "Florence"],
    "total_visits": 8
  }
}

# NOTE: list is ordered -> search by position
# NOTE: dict is unordered -> search by key
print(complex_travel_log["France"]["cities_visited"][1]) # get items in nested , use strings, 'key' values 
complex_travel_log["France"]["cities_visited"][1] = "Brussels" # change items in nested , use strings, 'key' values 
print(complex_travel_log["France"]["cities_visited"][1]) 

list1 = [travel_log, complex_travel_log] # put dicts in a list

country = input() 
visits = int(input()) 
list_of_cities = eval(input()) # create list from formatted string ** NOTE ** input is : ["Sao Paulo", "Rio de Janeiro"]
# eval() is used to evaluate a string as a Python expression. It takes a string as input and returns the evaluated result. Meaning string is like an python object
# if input is : ["Sao Paulo", "Rio de Janeiro"] , it considers it a list
# if input is : {1:"Govind"} , it considers it a dict

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  }
]
def add_new_country(country, visits, list_of_cities):
  dict_to_be_added = {} # first create inner object 
  dict_to_be_added["country"] = country
  dict_to_be_added["visits"] = visits
  dict_to_be_added["cities"] = list_of_cities
  travel_log.append(dict_to_be_added) # add inner object to outer object
  
### Highest Bidder 

def highest_bidder(main_dict):
    # initialize variables
    max_key = ""
    max_value = 0
    # Get highest value and its corresponding key
    for key in main_dict:
        if main_dict[key] > max_value:
            max_value = main_dict[key]
            max_key = key
    print(f"The highest bidder is {max_key} and the bid was {max_value}")
    

main_dict = {}
while_continue = True
while while_continue:
  name = input("name of bidder?")
  bid = int(input("Amount to bid : "))
  main_dict[name] = bid 
  to_continue = input("Any more bidder? y or n\n").lower()
  if to_continue == "y":
    clear_screen() # created at top
  else:
    while_continue = False
    highest_bidder(main_dict)




