from tkinter import *
from tkinter import messagebox
import random

#PASSWORD GENERATOR#

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    passw = []
    password = ""

    for char in range(nr_letters):
        passw += random.choice(letters)

    for char in range(nr_symbols):
        passw += random.choice(symbols)

    for char in range(nr_numbers):
        passw += random.choice(numbers)

    random.shuffle(passw)
    password = "".join(passw)
    
    password_input.focus()
    password_input.delete(0,END)
    password_input.insert(0,password)
    
#SAVE INFO#

def show_alert():
    messagebox.showinfo("Alert", "One or more fields left empty!")

def add_to_file():
    if website_input.get() != "" and email_user_input.get() != "" and password_input.get() != "":
        with open("accounts.txt", "a") as file:
            file.write(f'{website_input.get()} | {email_user_input.get()} | {password_input.get()}\n')
            website_input.delete(0,END)
            password_input.delete(0,END)
    else:
        show_alert()

#UI SETUP#

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

bg = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=bg)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=52)
website_input.grid(row=1, column=1, columnspan=2)
email_user_input = Entry(width=52)
email_user_input.focus()
email_user_input.insert(0, "dragos_juganariu@yahoo.com")
email_user_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=34)
password_input.grid(row=3, column=1)

generate_password = Button(text="Generate Password", width=14, command=generate_pass)
generate_password.grid(row=3, column=2)
add = Button(text="Add", width=44, command=add_to_file)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
