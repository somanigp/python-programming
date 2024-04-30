# ColumnSpan
# from tkinter import *
#
# window = Tk()
#
# r = Label(bg="red", width=20, height=5)
# r.grid(row=0, column=0)
#
# g = Label(bg="green", width=20, height=5)
# g.grid(row=1, column=1)
#
# b = Label(bg="blue", width=40, height=5)
# b.grid(row=2, column=0, columnspan=2)  # Stretches 40px across 2 columns.
#
#
# window.mainloop()

# Error Handling
# try:
#     # Code block where you anticipate an error
#     # For example, you might attempt to open a file, perform a calculation, or access a resource.
#     result = 10 / 0  # This will raise a ZeroDivisionError
# except ZeroDivisionError:
#     # Code block to handle the specific error
#     print("Cannot divide by zero!")
# except ValueError as e:
#     # You can have multiple except blocks to handle different types of errors
#     print(f"Invalid input! {e}")
# except Exception as e:
#     # This block catches any other exception not caught by the previous except blocks
#     print("An error occurred:", e)
# else:
#     # This block is executed if no exceptions were raised, if try is successful
#     print("No errors occurred.")
# finally:
#     # This block is always executed, regardless of whether an exception occurred or not
#     print("Execution complete.")

# try:
#     file = open('file.txt', mode='r')
#     print(file)
#     print(type(file))
#     file.close()
# except FileNotFoundError:
#     print("file not found")

# Exception Handling
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
except Exception as e:
    print(e)
else:
    content = file.read()
    print(content)
finally:  # Rarely used
    # raise TypeError("This is an error that I made up.")
    print("Executed")


# BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")  # Your own exception. ** Tap into one of the
    # known Exception classes. raise Exception(message).

bmi = weight / height ** 2
print(bmi)


facebook_posts = [{'Likes': 21, 'Comments': 2},
                  {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3},
                  {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]

total_likes = 0
# TODO: Catch the KeyError exception
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        # continue
        pass  # Both works to ignore

print(total_likes)