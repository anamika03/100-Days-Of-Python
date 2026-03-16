from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint

WHITE = "#fefefe"
YELLOW = "#efefea"
GREEN = "#127730"
BLACK = "#000000"
BLUE = "#2721D1"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    Password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = Website_entry.get()
    email = Email_entry.get()
    password = Password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n\nIs it ok to save?\n")   

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                Website_entry.delete(0, END)
                Email_entry.delete(0, END)
                Password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
Logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=Logo_img)
canvas.grid(column=1, row=0)

#Labels
Website_name = Label(text="Website:", bg=WHITE, fg=BLACK)
Website_name.grid(column=0, row=1)

Username = Label(text="Email/Username:", bg=WHITE, fg=BLACK)
Username.grid(column=0, row=2)

Password = Label(text="Password:", bg=WHITE, fg=BLACK)
Password.grid(column=0, row=3)

#Entries
Website_entry = Entry(width=39, bg=WHITE, fg=BLACK, highlightthickness=0, insertbackground=BLUE)
Website_entry.grid(column=1, row=1, columnspan=2)
Website_entry.focus()

Email_entry = Entry(width=39, bg=WHITE, fg=BLACK, highlightthickness=0, insertbackground=BLUE)
Email_entry.grid(column=1, row=2, columnspan=2)
Email_entry.insert(0, "rashika123@gmail.com")

Password_entry = Entry(width=22, bg=WHITE, fg=BLACK, highlightthickness=0, insertbackground=BLUE)
Password_entry.grid(column=1, row=3)

#Buttons
generate_password_button = Button(text="Generate Password", fg=BLACK, highlightthickness=0, highlightbackground=WHITE, command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, fg=BLACK, highlightthickness=0, highlightbackground=WHITE, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
