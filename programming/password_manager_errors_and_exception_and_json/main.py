# Imports and Sites
# For all tkinter docs: https://tkdocs.com/tutorial/canvas.html
# https://tcl.tk/man/tcl8.6/TclCmd/contents.htm
# https://tcl.tk/man/tcl8.6/TkCmd/contents.htm

from tkinter import *  # NOTE: ** It actually only imports all the classes and constants
from tkinter import messagebox  # Just another module of code. Right click -> Go To -> Implementations
from random_password_generator import random_password_generator
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password_function():
    password = random_password_generator()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # copy password in clipboard


def search_creds():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showwarning(title="Warning", message="Please type the website to select.")
    else:
        try:
            with open("data.json", "r") as data_file:
                json_data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title=website, message="Data Not Found")
        except json.decoder.JSONDecodeError:  # Got error from logs.
            messagebox.showerror(title=website, message="Data Not Found")
        else:
            # if website in json_data: # This also works
            creds = json_data.get(website)
            if creds is None:
                messagebox.showerror(title=website, message=f"No details for {website} exists")
            else:
                messagebox.showinfo(website, f"Email/Username: {creds.get('email_or_username')}\n"
                                             f"Password: {creds.get('password')}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password() -> None:
    """Save the info in file data.txt"""
    website = website_entry.get()
    email_or_username = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any field empty.")
    else:
        # is_ok will be boolean
        is_ok = messagebox.askokcancel(title=website, message=f"Are you sure you want to save these changes?\nEmail:"
                                                              f"{email_or_username}\nPassword:{password}")
        if is_ok:
            # data_to_save = " | ".join([website, email_or_username, password])
            # with open('data.txt', mode='a') as file:
            #     file.write(data_to_save + '\n')
            data = {website: {
                "email_or_username": email_or_username,
                "password": password
            }}
            try:
                with open("data.json", "r") as data_file:
                    json_data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            else:
                json_data.update(data)
                with open("data.json", "w") as data_file:
                    json.dump(json_data, data_file, indent=4)
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
                website_entry.focus()  # Again shifting focus to website entry


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
photo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo_image)
canvas.grid(row=1, column=2)

# Labels
website_name = Label(text="Website:")
website_name.grid(row=2, column=1, sticky="E")  # sticky is for placement within the grid.

email_name = Label(text="Email/Username:")
email_name.grid(row=3, column=1, sticky="E")

password_name = Label(text="Password:")
password_name.grid(row=4, column=1, sticky="E")

# Entries
website_entry = Entry(width=30)
website_entry.grid(row=2, column=2, columnspan=2, sticky="W")
website_entry.focus()  # If focus used with 2 components, the later one will be implemented. Focus -> pointer in start.

email_entry = Entry(width=43)
email_entry.grid(row=3, column=2, columnspan=2, sticky="W")
email_entry.insert(0, 'somanigp12@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(row=4, column=2, sticky="W")

# Buttons
generate_password = Button(text="Generate Password", command=generate_password_function)
generate_password.grid(row=4, column=2, sticky="E", columnspan=2)  # Can put 2 widgets in the same grid.

add_creds = Button(text="ADD", width=36, command=save_password)
add_creds.grid(row=5, column=2, columnspan=2, sticky="W")

search_button = Button(text="search", width=10, command=search_creds)
search_button.grid(row=2, column=2, columnspan=2, sticky="E")

window.mainloop()
