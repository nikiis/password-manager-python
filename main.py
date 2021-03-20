import string
import tkinter as tk
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for x in range(14):
        password += random.choice(password_characters)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:

        is_ok = messagebox.askokcancel(title="website",
                                       message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open('data.txt', mode='a') as file:
                file.write(f"{website} | {username} | {password} \n")

        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width="200", height="200")
logo = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = tk.Label()
website_label.config(text="Website:")
website_label.grid(row=1, column=0)

website_entry = tk.Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = tk.Label()
email_label.config(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = tk.Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "nicoleshek315@gmail.com")

password_label = tk.Label()
password_label.config(text="Password:")
password_label.grid(row=3, column=0)

password_entry = tk.Entry(width=19)
password_entry.grid(row=3, column=1)

generate_button = tk.Button()
generate_button.config(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky='w')

add_button = tk.Button(width=34)
add_button.config(text="Add", command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
