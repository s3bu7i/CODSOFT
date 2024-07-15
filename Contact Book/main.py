import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

def init_db():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

class ContactBookApp(tk.Tk):
    def __init__(self):
        super().__init__()

        init_db()

        self.title("Contact Book")
        self.geometry("600x400")
        self.configure(bg='purple')

        self.create_widgets()

    def create_widgets(self):
        self.contact_list = ttk.Treeview(self, columns=(
            "ID", "Name", "Phone", "Email", "Address"), show="headings")
        self.contact_list.heading("ID", text="ID")
        self.contact_list.heading("Name", text="Name")
        self.contact_list.heading("Phone", text="Phone")
        self.contact_list.heading("Email", text="Email")
        self.contact_list.heading("Address", text="Address")
        self.contact_list.column("ID", width=30)
        self.contact_list.pack(fill=tk.BOTH, expand=True, pady=10)

        self.load_contacts()
        self.button_frame = tk.Frame(self, bg='purple')
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(
            self.button_frame, text="Add Contact", command=self.open_add_window)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.update_button = tk.Button(
            self.button_frame, text="Edit Contact", command=self.open_edit_window)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(
            self.button_frame, text="Delete Contact", command=self.open_delete_window)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

    def load_contacts(self):
        for item in self.contact_list.get_children():
            self.contact_list.delete(item)

        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        conn.close()

        for contact in contacts:
            self.contact_list.insert("", tk.END, values=contact)

    def open_add_window(self):
        AddContactWindow(self)

    def open_edit_window(self):
        selected_item = self.contact_list.selection()
        if selected_item:
            contact = self.contact_list.item(selected_item, "values")
            EditContactWindow(self, contact)
        else:
            messagebox.showwarning(
                "Selection Error", "Please select a contact to edit")

    def open_delete_window(self):
        selected_item = self.contact_list.selection()
        if selected_item:
            contact_id = self.contact_list.item(selected_item, "values")[0]
            DeleteContactWindow(self, contact_id)
        else:
            messagebox.showwarning(
                "Selection Error", "Please select a contact to delete")

class AddContactWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Contact")
        self.geometry("300x200")
        self.configure(bg='purple')

        self.create_widgets()
    def create_widgets(self):
        self.name_label = tk.Label(self, text="Name:", bg='purple', fg='white')
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(
            self, text="Phone:", bg='purple', fg='white')
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(
            self, text="Email:", bg='purple', fg='white')
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_label = tk.Label(
            self, text="Address:", bg='purple', fg='white')
        self.address_label.grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(
            self, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone and email and address:
            conn = sqlite3.connect('contacts.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                           (name, phone, email, address))
            conn.commit()
            conn.close()

            self.master.load_contacts()
            self.destroy()
        else:
            messagebox.showwarning("Input Error", "All fields are required")
class EditContactWindow(tk.Toplevel):
    def __init__(self, parent, contact):
        super().__init__(parent)
        self.title("Edit Contact")
        self.geometry("300x200")
        self.configure(bg='purple')

        self.contact_id = contact[0]
        self.create_widgets(contact)
    def create_widgets(self, contact):
        self.name_label = tk.Label(self, text="Name:", bg='purple', fg='white')
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.insert(0, contact[1])
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(
            self, text="Phone:", bg='purple', fg='white')
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.insert(0, contact[2])
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(
            self, text="Email:", bg='purple', fg='white')
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.insert(0, contact[3])
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_label = tk.Label(
            self, text="Address:", bg='purple', fg='white')
        self.address_label.grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self)
        self.address_entry.insert(0, contact[4])
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.update_button = tk.Button(
            self, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=4, columnspan=2, pady=10)

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone and email and address:
            conn = sqlite3.connect('contacts.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ?, address = ? WHERE id = ?",
                           (name, phone, email, address, self.contact_id))
            conn.commit()
            conn.close()

            self.master.load_contacts()
            self.destroy()
        else:
            messagebox.showwarning("Input Error", "All fields are required")

class DeleteContactWindow(tk.Toplevel):
    def __init__(self, parent, contact_id):
        super().__init__(parent)
        self.title("Delete Contact")
        self.geometry("300x100")
        self.configure(bg='purple')

        self.contact_id = contact_id

        self.create_widgets()

    def create_widgets(self):
        self.confirm_label = tk.Label(
            self, text="Are you sure you want to delete this contact?", bg='purple', fg='white')
        self.confirm_label.pack(pady=10)

        self.button_frame = tk.Frame(self, bg='purple')
        self.button_frame.pack(pady=10)

        self.yes_button = tk.Button(
            self.button_frame, text="Yes", command=self.delete_contact)
        self.yes_button.grid(row=0, column=0, padx=5)

        self.no_button = tk.Button(
            self.button_frame, text="No", command=self.destroy)
        self.no_button.grid(row=0, column=1, padx=5)
    def delete_contact(self):
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = ?", (self.contact_id,))
        conn.commit()
        conn.close()

        self.master.load_contacts()
        self.destroy()


# Run the code
if __name__ == "__main__":
    app = ContactBookApp()
    app.mainloop()
