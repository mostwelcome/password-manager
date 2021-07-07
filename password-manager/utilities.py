import random
import json
import pyperclip
from tkinter import messagebox
from constants import LETTERS, DIGITS, SYMBOLS, NO_OF_LETTERS, NO_OF_DIGITS, NO_OF_SYMBOLS, END
from messages import WEBSITE_DETAILS_MSG, NO_DATA_ERR, NO_DATA_WEBSITE_ERR, EMPTY_FIELD_ERR


def generate_password(password_entry):
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


def search_password(website_entry):
    try:
        website = website_entry.get()
        if not website:
            messagebox.showinfo(message=WEBSITE_DETAILS_MSG)
        else:
            with open('data.json', 'r') as data_file:
                data_found = json.load(data_file)
                password_details = data_found[website]
                messagebox.showinfo(
                    title=website, message=f" Email : {password_details.get('email')} \n Password: {password_details.get('password')}")
    except FileNotFoundError:
        messagebox.showinfo(message=NO_DATA_ERR)
    except KeyError:
        messagebox.showinfo(message=NO_DATA_WEBSITE_ERR)


def save(website_entry, email_entry, password_entry):
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        'email': email,
        'password': password
    }}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
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
