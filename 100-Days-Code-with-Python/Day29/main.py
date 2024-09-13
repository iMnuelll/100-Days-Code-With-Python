from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    """
    Generates a random password consisting of letters, numbers, and symbols.
    The password will have 8-10 letters, 2-4 symbols, and 2-4 numbers.
    The password is shuffled to randomize the order of the characters.
    The generated password is displayed in the password entry field and copied to the clipboard.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly choose letters, numbers, and symbols for the password.
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine the chosen characters and shuffle them to randomize the order.
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    
    # Convert the list of characters into a string and insert it into the password entry field.
    password = "".join(password_list)
    password_entry.insert(0, password)
    
    # Copy the generated password to the clipboard.
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    Saves the website, email, and generated password into a text file (data.txt).
    If any fields are left empty, a warning is shown to the user.
    A confirmation message box is displayed to ensure the user wants to save the information.
    After saving, the website and password fields are cleared for the next entry.
    """
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if any fields are empty. If so, show a warning message and return.
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # Ask the user for confirmation before saving the data.
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        # Save the data into the file and clear the entry fields.
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Set up the main window and configure its layout
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.columnconfigure((0,1,2), weight=1)
window.rowconfigure((0,1,2), weight=1)

# Set up the logo image on a canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=2, sticky="NSEW")

#Labels for website, email and password
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="W")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="W")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="W")

#Entries
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, sticky="W", columnspan=2)
website_entry.focus() # Automatically focus on the website entry field
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, sticky="W", columnspan=2)
email_entry.insert(0, "your_email@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="W")

# Buttons to generate a password and save the information.
generate_password_button = Button(width=15, text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky='W')
add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

# Start the Tkinter main even loop.
window.mainloop()