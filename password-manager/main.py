from tkinter import *
from utilities import generate_password, search_password, save


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)

canvas.grid(row=0, column=1)

# labels
website_label = Label(text='Website')
website_label.grid(row=1, column=0)
email_label = Label(text='Email')
email_label.grid(row=2, column=0)
password_label = Label(text='Password')
password_label.grid(row=3, column=0)


# Entries
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
# default email
email_entry.insert(0, 'abc@gmail.com')
password_entry = Entry(width=40)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
generate_password_button = Button(
    text='Generate Password', command=lambda: generate_password(password_entry))
generate_password_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text='Search Password',
                       command=lambda: search_password(website_entry))
search_button.grid(row=5, column=1, columnspan=2)
save_button = Button(text='Save Password', width=30, command=lambda: save(
    website_entry, email_entry, password_entry))
save_button.grid(row=6, column=1, columnspan=2)
window.mainloop()
