# NOTES: open, read, write and close the file
# open - inbuilt methode of python. Inputs: file, mode, etc

# By default, the mode is read only.
file = open("./data.txt")  # the name of the file is input as string, also here we are opening the file and
# saving it in a variable.

contents = file.read()  # returns the content of the file as a string.
print(contents)
file.close()  # Closing a file manually, once a file is open, it takes up some resources of the computer.
# So at some point in time, python might close the file to free up those resources. Thus, close it manually,
# so we know when its closing.

# Use 'with' keyword to open the file and use it. Then it gets closed automatically when work is done. 'with'
# will manage this file
with open("data.txt") as f:
    print(f.read())

# for write access use mode = 'w'. Now you cant read with this access.
# Also if the mode is 'w', then if the file doesn't exist, then it will create the file.
with open("data.txt", mode='w') as f:
    f.write(f"This will replace the old line.!")  # This will replace all the old text inside the file with whatever
    # is in the string.

# for 'append' access, add extra to a file. Use mode = 'a'
with open("data.txt", mode='a') as f:
    f.write(f"\nThis adds a line here.")  # \n This is for new line


with open("new_file.txt", mode='w') as file:
    file.write("Creates a new file")

# with open("/C:/Users/soman/") as file:  # Absolute Path : "/C:/Users/soman/..." '/' is root as we have C and D drive
#     file.read()

# Absolute Path: No need for root '/C:/', we can just go '/'
with open("/Users/soman/OneDrive/Desktop/Govind's Library/Coding/python/python-programming/programming/"
          "files_and_directories/data.txt") as file:
    print("Here")
    print(file.read())

# File Paths:
# Root : hard disk (mackintoshHD in apple and C or D drive) is the root folder generally.

# Below are absolute path:
# In Windows PC: Use '\' like this 'C:\Users\soman\OneDrive\Desktop\Govind's Library\Coding\python\python-programming'
# For Linus/Chrome and Coding use '/' and starts with 'file:///' like this:
# 'file:///C:/Users/soman/OneDrive/Desktop/Govind's%20Library/Coding/python/python-programming/'. '/' in the end.

# In coding also use '/' slash
# Absolute Path starts from the root, and a Relative path starts from the current directory.
# In coding root can be just represented by '/'. so
# '/User/soman/OneDrive/Desktop/Govind's%20Library/Coding/python/python-programming/'
# for linux environment its different, in linux root is '/'
# working directory: our current dir.
# ./talk.ppt # look in the current folder for talk.ppt. NOTE: you can shorten it to talk.ppt
# ./Project/talk.ppt # go in the Project folder in current dir and then in that goto talk.ppt
# ../report.doc # go to parent dir and chose report.doc
