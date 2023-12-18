############DEBUGGING#####################

# # Describe Problem to get the issue , make assumptions and check if false or true
# def my_function():
#   for i in range(1, 20): # added 1 so for loop can include i = 20
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug - so you can analyze it, change the code so it always produces that error and then try to fix it
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # List index doesnt have index 6, only till 0 to 5, so will give index out of range error
# print(dice_imgs[dice_num])

# # Play Computer - think what computer will do to see flow of chart
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: # for 1994, neither if statement covers them
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors - when IDE gives error( red lines ) - fix them on the spot , mostly syntax errors
# age = input("How old are you?") # needs to be an int , some error you only see in console after you run the code . Search them online
# if age > 18:
# print(f"You can drive at age {age}.") # f-string , add 'f' to format and indentation needs to be added

# #Print is Your Friend - use print to see the errors in console and correct them. You can check flows and values, etc
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # the sign is == and not = , so comparision is happening and not assignment
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger - put stops/breakpoints , go into functions and check line by line , check variables value,etc. Python tutor - visualize execution option , thonny , google dev tools and IDEs
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) # note no identation, new_item is just twice of last item in a_list
#   print(b_list) # will be 26

# mutate([1,2,3,5,8,13])


# Final Tips :
# Break , Ask a friend 
# Run Code Often 
# Search Net 

