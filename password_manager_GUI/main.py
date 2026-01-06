"""
Password Manager (Python)

A lightweight desktop password manager built with Tkinter.
Features:
- Secure password generation using the `secrets` module
- User inputs for website and username/email
- One-click password generation
- Save functionality (local storage logic handled separately)

This project focuses on Python fundamentals and security-conscious design,
not advanced GUI development.

Note: GUI is intentionally minimal; emphasis is on logic, randomness quality,
and practical usability.
"""

from tkinter import *
from tkinter import messagebox
from combinations import create_password
import json

FILEPATH = "data.json"

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(window, width=200, height=200, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

logo = PhotoImage(file="logo.png").subsample(4, 4)
canvas.image = logo
canvas.create_image(100, 100, image=logo)


def generate_password():
    password_entry.delete(0, END)
    password_entry.insert(0, create_password())

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(username) > 0 and len(website) > 0:
        new_entry = {
            website: {
                "username": username,
                "password": password
            }
        }
        try:
            # Load existing data
            with open(FILEPATH, 'r') as file:
                data = json.load(file)
            data.update(new_entry)
            with open(FILEPATH, 'w') as file:
                json.dump(data, file, indent= 4)
        except FileNotFoundError:
            data = {}
            data.update(new_entry)
            with open(FILEPATH, 'w') as file:
                json.dump(data, file, indent= 4)
    else:
       messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")


        
def search_password():
    website = website_entry.get()
    if len(website) > 0:
        try:
            with open(FILEPATH, 'r') as file:
                data = json.load(file)
            searched = data.get(website_entry.get())
            password = searched.get("password")
            userid = searched.get("username")

            password_entry.insert(0, password) 
            username_entry.insert(0, userid)   

        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="you haven't saved any passwoords")

        except AttributeError:
            messagebox.showinfo(title="Oops", message=f"you haven't saved a password for{website}")
    else:
         messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")


Label(text="Website:").grid(row=1, column=0)
Label(text="Email / Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_entry = Entry(width=21)
username_entry.grid(row=2, column=1, columnspan=1)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


Button(text="Search Password", command=search_password).grid(row=1, column=2)
Button(text="Generate Password", command=generate_password).grid(row=3, column=2)
Button(text="Save", width=36, command=save_password).grid(row=4, column=1, columnspan=2)

window.mainloop()

