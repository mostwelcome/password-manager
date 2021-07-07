"""Utilities for password manager."""
import random
import json
from tkinter import messagebox, Entry
import pyperclip
from constants.constants import LETTERS, DIGITS, SYMBOLS, NO_OF_LETTERS, NO_OF_DIGITS, NO_OF_SYMBOLS, END
from constants.messages import WEBSITE_DETAILS_MSG, NO_DATA_ERR, NO_DATA_WEBSITE_ERR, EMPTY_FIELD_ERR, SUCCESS_MSG, FAILURE_MSG


def generate_password(password_entry: Entry) -> None:
    """Generate password."""
    if len(password_entry.get()) != 0:
        password_entry.delete(0, END)
        password_entry.insert(0, '')
    # Password Generator

    pass_letters = [random.choice(LETTERS) for _ in range(NO_OF_LETTERS)]
    pass_digits = [random.choice(DIGITS) for _ in range(NO_OF_DIGITS)]
    pass_symbols = [random.choice(SYMBOLS) for _ in range(NO_OF_SYMBOLS)]

    password = pass_letters + pass_digits + pass_symbols
    random.shuffle(password)
    password = ''.join(password)
    password_entry.insert(0, password)
    # copy the password to clip board as we don't need to copy paste manually
    pyperclip.copy(password)


def search_password(website_entry: Entry) -> None:
    """Search password."""
    website = website_entry.get()
    if not website:
        messagebox.showinfo(title=FAILURE_MSG, message=WEBSITE_DETAILS_MSG)
    else:
        try:
            with open('data.json', 'r') as data_file:
                data_found = json.load(data_file)
                password_details = data_found.get(website)
                if password_details:
                    title, message = SUCCESS_MSG, f"Email : {password_details.get('email')} \n Password: {password_details.get('password')}"
                else:
                    title, message = FAILURE_MSG, NO_DATA_WEBSITE_ERR
                messagebox.showinfo(title=title, message=message)
        except FileNotFoundError:
            messagebox.showinfo(message=NO_DATA_ERR)


def save(website_entry: Entry, email_entry: Entry, password_entry: Entry) -> Entry:
    """Save password."""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        'email': email,
        'password': password
    }}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title=FAILURE_MSG,
                            message=EMPTY_FIELD_ERR)
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f'These are the details entered :\nEmail : {email}\nPassword :{password}\nIs it okay to save?\n')

        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    # Read the old data
                    data = json.load(data_file)
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            finally:
                # clearing entries
                website_entry.delete(0, END)
                password_entry.delete(0, END)
