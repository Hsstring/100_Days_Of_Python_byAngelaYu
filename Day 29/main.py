from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for sym in range(nr_symbols)]
    password_list += [random.choice(numbers) for num in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Password is copied on clipboard
# --------------------------------SEARCH------------------------------------ #


def find_password():
    entry_web = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title=entry_web, message="No Data File Found")
    else:
        try:
            key = data[entry_web]
        except KeyError:
            messagebox.showerror(title=entry_web, message="No details for the website exists")
        else:
            messagebox.showinfo(title=entry_web, message=f"EMAIL: {key['email']}\n"
                                                         f"PASSWORD: {key['password']}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }
    if len(website_entry.get()) < 1 or len(password_entry.get()) < 1:
        messagebox.showerror(title="Error", message="You've left some fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
canvas = Canvas(width=200, height=200, highlightthickness=0)
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_img)
window.config(pady=30, padx=30)
canvas.grid(column=1, row=0, sticky=W)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=34)
website_entry.grid(column=1, row=1, sticky=W)
website_entry.focus()
email_entry = Entry(width=34)
email_entry.grid(column=1, row=2, columnspan=2, sticky=W)
email_entry.insert(0, "Hana.ahmadzadeh80@gmail.com")
password_entry = Entry(width=34)
password_entry.grid(column=1, row=3, sticky=W)

generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
