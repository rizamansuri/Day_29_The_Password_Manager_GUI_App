# In the name of Allah, the most Beneficent and the most Merciful.....
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- SEARCH PASSWORD DATA ------------------------------- #
def search():
    website = website_input.get().title()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password} ")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"No details for the {website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_pass():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()

    new_data = {website:
        {
            "email": email,
            "password": password
        }
    }

    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showwarning(title="Ooops", message="Please make sure you haven't left any field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            if website in data:
                messagebox.showwarning(title="Duplicate", message=f"{website} details already exists.")
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Writing updated data to the file
                    json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

X_PAD = 5
Y_PAD = 5
BG_COLOR = "#CCD6A6"
FONT = ("Courier", 11, "bold")
window = Tk()
window.title("Riza's Password Manager")
window.config(padx=50, pady=50, bg=BG_COLOR)

canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

## LABLES
# Website Label
website_label = Label(text="Website:", bg=BG_COLOR)
website_label.grid(row=1, column=0, padx=X_PAD, pady=Y_PAD)
# Email & Username label
email_label = Label(text="Email/Username:", bg=BG_COLOR)
email_label.grid(row=2, column=0, padx=X_PAD, pady=Y_PAD)
# Password label
password_label = Label(text="Password:", bg=BG_COLOR)
password_label.grid(row=3, column=0, padx=X_PAD, pady=Y_PAD)

## ENTRIES
# Website input
website_input = Entry()
website_input.grid(row=1, column=1, sticky=EW, padx=X_PAD, pady=Y_PAD)
website_input.focus()
# Email & Username input
email_input = Entry()
email_input.grid(row=2, column=1, columnspan=2, sticky=EW, padx=X_PAD, pady=Y_PAD)
email_input.insert(0, "riza.mansuri11@gmail.com")
# Password input
password_input = Entry()
password_input.grid(row=3, column=1, sticky=EW, padx=X_PAD, pady=Y_PAD)

## BUTTONS
# Generate Password button
generate_password = Button(text="Generate Password", bg="#AA8B56", command=generate_pass)
generate_password.grid(row=3, column=2, sticky=EW, padx=X_PAD, pady=Y_PAD)
# Add button
add_button = Button(text="Add", width=30, bg="#AA8B56", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW, padx=X_PAD, pady=Y_PAD)
# Search Button
search_button = Button(text="Search", bg="#AA8B56", command=search)
search_button.grid(row=1, column=2, sticky=EW, padx=X_PAD, pady=Y_PAD)
window.mainloop()
