import json
from tkinter import *
from tkinter import messagebox
import pyperclip
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_number + password_symbol + password_letter
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    email = email_entry.get()
    password = password_input.get()
    website = website_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please check your input again")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading
                loaded_data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating
            loaded_data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving
                json.dump(loaded_data, data_file, indent=4)
        finally:
            password_input.delete(0, END)
            website_entry.delete(0, END)


# SEARCH FOR WEB PASSWORD

def search_web():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title=website, message=f"No data for  {website}  exists!")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="No data file found!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=500)
window.config(padx=20, pady=20)

image = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=22)
website_entry.focus()
website_entry.grid(row=1, column=1)
email_entry = Entry(width=40)
email_entry.insert(0, "phelixdusengimana@gmail.com")
email_entry.grid(row=2, column=1, columnspan=3)
password_input = Entry(width=22)
password_input.grid(row=3, column=1)

search_btn = Button(text="Search", command=search_web)
search_btn.grid(row=1, column=2)
generate_btn = Button(text="Generate Password", command=password_generator)
generate_btn.grid(row=3, column=2)
save_button = Button(text="Add", width=35, command=save_password)
save_button.grid(row=4, column=1, columnspan=3)

window.mainloop()
