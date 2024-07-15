import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=30, padx=30)

        self.length_label = tk.Label(self.main_frame, text="Password Length:")
        self.length_label.grid(row=0, column=0, sticky='w')
        self.length_entry = tk.Entry(self.main_frame, width=10)
        self.length_entry.grid(row=0, column=1, pady=5)

        self.uppercase_var = tk.BooleanVar()
        self.uppercase_check = tk.Checkbutton(
            self.main_frame, text="Include Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_check.grid(row=1, column=0, columnspan=2, sticky='w')

        self.lowercase_var = tk.BooleanVar(value=True)
        self.lowercase_check = tk.Checkbutton(
            self.main_frame, text="Include Lowercase Letters", variable=self.lowercase_var)
        self.lowercase_check.grid(row=2, column=0, columnspan=2, sticky='w')

        self.digits_var = tk.BooleanVar(value=True)
        self.digits_check = tk.Checkbutton(
            self.main_frame, text="Include Digits", variable=self.digits_var)
        self.digits_check.grid(row=3, column=0, columnspan=2, sticky='w')

        self.special_var = tk.BooleanVar()
        self.special_check = tk.Checkbutton(
            self.main_frame, text="Include Special Characters", variable=self.special_var)
        self.special_check.grid(row=4, column=0, columnspan=2, sticky='w')

        self.similar_var = tk.BooleanVar()
        self.similar_check = tk.Checkbutton(
            self.main_frame, text="Avoid Similar Characters", variable=self.similar_var)
        self.similar_check.grid(row=5, column=0, columnspan=2, sticky='w')

        self.ambiguous_var = tk.BooleanVar()
        self.ambiguous_check = tk.Checkbutton(
            self.main_frame, text="Exclude Ambiguous Characters", variable=self.ambiguous_var)
        self.ambiguous_check.grid(row=6, column=0, columnspan=2, sticky='w')

        self.custom_label = tk.Label(
            self.main_frame, text="Custom Characters:")
        self.custom_label.grid(row=7, column=0, sticky='w')
        self.custom_entry = tk.Entry(self.main_frame, width=20)
        self.custom_entry.grid(row=7, column=1, pady=5)

        self.generate_button = tk.Button(
            self.main_frame, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.password_label = tk.Label(
            self.main_frame, text="Generated Password:")
        self.password_label.grid(row=9, column=0, sticky='w')
        self.password_display = tk.Entry(
            self.main_frame, state='readonly', width=50)
        self.password_display.grid(row=9, column=1)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Length must be positive")
        except ValueError:
            messagebox.showerror(
                "Invalid input", "Please enter a valid number for length")
            return

        characters = ''
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.digits_var.get():
            characters += string.digits
        if self.special_var.get():
            characters += string.punctuation

        if self.similar_var.get():
            characters = ''.join(c for c in characters if c not in 'il1Lo0O')

        if self.ambiguous_var.get():
            characters = ''.join(
                c for c in characters if c not in '{}[]()/\\\'"~,;:.<>')

        custom_chars = self.custom_entry.get()
        if custom_chars:
            characters += custom_chars

        if not characters:
            messagebox.showerror(
                "Invalid selection", "Please select at least one character set or enter custom characters")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.config(state='normal')
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)
        self.password_display.config(state='readonly')


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
