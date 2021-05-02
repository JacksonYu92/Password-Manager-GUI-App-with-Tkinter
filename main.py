from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = random_letters + random_symbols + random_numbers

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
                website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=35)
username_entry.insert(0, "jacksonyu@email.com")
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=27)
password_entry.grid(row=3, column=1, sticky="W")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")








window.mainloop()