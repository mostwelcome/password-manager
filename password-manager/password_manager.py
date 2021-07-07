from tkinter import *
from utilities import generate_password, search_password, save


class PasswordManager:
    "Password manager."

    def __init__(self) -> None:
        self.window = Tk()

    def _set_window(self):
        self.window.title('Password Manager')
        self.window.config(padx=50, pady=50)

    def _set_canvas(self):
        self.canvas = Canvas(height=200, width=200)
        self.canvas.create_image(
            100, 100, image=PhotoImage(file='static/logo.png'))
        self.canvas.grid(row=0, column=1)

    def _set_labels(self):
        self.website_label = Label(text='Website')
        self.website_label.grid(row=1, column=0)

        self.email_label = Label(text='Email')
        self.email_label.grid(row=2, column=0)

        self.password_label = Label(text='Password')
        self.password_label.grid(row=3, column=0)

    def _set_entries(self):
        self.website_entry = Entry(width=40)
        self.website_entry.grid(row=1, column=1, columnspan=2)
        self.website_entry.focus()

        self.email_entry = Entry(width=40)
        self.email_entry.grid(row=2, column=1, columnspan=2)
        self.email_entry.insert(0, 'abc@gmail.com')  # default email

        self.password_entry = Entry(width=40)
        self.password_entry.grid(row=3, column=1, columnspan=2)

    def _set_buttons(self):
        self.password_button = Button(
            text='Generate Password', command=lambda: generate_password(self.password_entry))
        self.password_button.grid(row=4, column=1, columnspan=2)
        self.search_button = Button(text='Search Password',
                                    command=lambda: search_password(self.website_entry))
        self.search_button.grid(row=5, column=1, columnspan=2)
        self.save_button = Button(text='Save Password', width=30, command=lambda: save(
            self.website_entry, self.email_entry, self.password_entry))
        self.save_button.grid(row=6, column=1, columnspan=2)

    def render_window(self):
        self.window.mainloop()
