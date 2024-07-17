import string
import random
import pyperclip
from tkinter import messagebox

def generate_password(length, use_symbols, use_digits):
    """Generates a password of a given length."""
    base_chars = string.ascii_letters
    if use_symbols:
        base_chars += string.punctuation
    if use_digits:
        base_chars += string.digits

    password = ''.join(random.choice(base_chars) for _ in range(length))
    return password


def password_strength(password):
    """Determines the strength of a password."""
    length_error = len(password) < 8
    digit_error = not any(char.isdigit() for char in password)
    uppercase_error = not any(char.isupper() for char in password)
    lowercase_error = not any(char.islower() for char in password)
    symbol_error = not any(char in string.punctuation for char in password)
    password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)

    strength = 'Weak'
    if password_ok:
        strength = 'Strong'
    elif not length_error and not (digit_error and uppercase_error and lowercase_error and symbol_error):
        strength = 'Medium'

    return strength

def generate_and_show(entry_length, entry_password, strength_label, use_symbols, use_digits):
    """Generates a password and shows it in the GUI."""
    password_length = entry_length.get()

    # Check if the password length input is valid
    if not password_length.isdigit():
        print("Invalid input! Please enter a valid integer for password length.")
        return

    length = int(password_length)
    password = generate_password(length, bool(use_symbols), bool(use_digits))
    strength = password_strength(password)

    # Put the generated password in entry_password
    entry_password.delete(0, 'end')
    entry_password.insert(0, password)
    
    # Update the strength label
    strength_label.config(text=strength)

def password_mask(entry, var):
    """Masks or unmasks a password in the GUI."""
    if var.get():
        entry.config(show='*')
    else:
        entry.config(show='')

def copy_to_clipboard(entry_2):
    """Copies a password to the clipboard."""
    password = entry_2.get()
    pyperclip.copy(password)
    messagebox.showinfo("Password Copied", "Password copied to clipboard.")
