import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import sqlite3

# Database setup
conn = sqlite3.connect('./To-Do-List/tasks.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY, task TEXT, detail TEXT, deadline TEXT, status TEXT)''')
conn.commit()


def add_or_edit_task():
    task = task_entry.get()
    detail = detail_entry.get()
    deadline = deadline_entry.get()
    if task and deadline:
        if add_button['text'] == 'Add Task':
            c.execute("INSERT INTO tasks (task, detail, deadline, status) VALUES (?, ?, ?, ?)",
                      (task, detail, deadline, 'Pending'))
        else:
            task_id = selected_task_id
            c.execute("UPDATE tasks SET task=?, detail=?, deadline=? WHERE id=?",
                      (task, detail, deadline, task_id))
            add_button.config(text='Add Task')
        conn.commit()
        display_tasks()
        clear_entries()
    else:
        messagebox.showwarning(
            "Input Error", "Please fill task name and deadline")


def delete_task():
    selected_item = task_list.curselection()
    if selected_item:
        task_id = task_list.get(selected_item).split()[0]
        c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        display_tasks()
        clear_entries()
        add_button.config(text='Add Task')
    else:
        messagebox.showwarning(
            "Selection Error", "Please select a task to delete")


def select_task(event):
    global selected_task_id
    selected_item = task_list.curselection()
    if selected_item:
        task_id = task_list.get(selected_item).split()[0]
        selected_task_id = task_id
        c.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
        task = c.fetchone()
        if task:
            task_entry.delete(0, tk.END)
            task_entry.insert(0, task[1])
            detail_entry.delete(0, tk.END)
            detail_entry.insert(0, task[2])
            deadline_entry.delete(0, tk.END)
            deadline_entry.insert(0, task[3])
            add_button.config(text='Save Task')


def display_tasks():
    task_list.delete(0, tk.END)
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    for task in tasks:
        task_list.insert(
            tk.END, f"{task[0]} - {task[1]} - {task[2]} - {task[3]} - {task[4]}")


def check_deadlines():
    current_time = datetime.now()
    c.execute("SELECT * FROM tasks WHERE status='Pending'")
    tasks = c.fetchall()
    for task in tasks:
        try:
            deadline = datetime.strptime(task[3], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            deadline = datetime.strptime(task[3], '%Y-%m-%d')
        if current_time > deadline:
            task_list.insert(tk.END, f"DEADLINE PASSED - {task[1]}")

    task_list.after(60000, check_deadlines)  # Check every 60 seconds


def update_deadline_format():
    if date_only_var.get():
        deadline_label.config(text="Deadline (YYYY-MM-DD):")
    else:
        deadline_label.config(text="Deadline (YYYY-MM-DD HH:MM:SS):")


def clear_entries():
    task_entry.delete(0, tk.END)
    detail_entry.delete(0, tk.END)
    deadline_entry.delete(0, tk.END)
    add_button.config(text='Add Task')


# GUI setup
root = tk.Tk()
root.title("To-Do App")
root.config(bg='#A020F0')

# Task name input
task_label = tk.Label(root, text="Task Name:", bg='#D9A7E8',
                      fg='black', font=('Roboto', 12, 'bold'))
task_label.pack(pady=5)
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

# Task detail input
detail_label = tk.Label(root, text="Task Detail:",
                        bg='#D9A7E8', fg='black', font=('Roboto', 12, 'bold'))
detail_label.pack(pady=5)
detail_entry = tk.Entry(root, width=50)
detail_entry.pack(pady=3)

# Deadline type selection
date_only_var = tk.BooleanVar(value=True)
date_only_radio = tk.Radiobutton(root, text="Date Only", variable=date_only_var,
                                 value=True, command=update_deadline_format, bg='#D9A7E8', fg='black')
date_and_time_radio = tk.Radiobutton(root, text="Date and Time", variable=date_only_var,
                                     value=False, command=update_deadline_format, bg='#D9A7E8', fg='black')
date_only_radio.pack(pady=4)
date_and_time_radio.pack(pady=4)

# Deadline input
deadline_label = tk.Label(root, text="Deadline (YYYY-MM-DD):",
                          bg='#D9A7E8', fg='black', font=('Airawat', 12, 'bold'))
deadline_label.pack(pady=4)
deadline_entry = tk.Entry(root, width=50)
deadline_entry.pack(pady=4)

# Buttons
button_frame = tk.Frame(root, bg='#D9A7E8')
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task",
                       command=add_or_edit_task, bg='#FFD700', font=('Roboto', 10, 'bold'))
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task",
                          command=delete_task, bg='#FFD700', font=('Roboto', 10, 'bold'))
delete_button.grid(row=0, column=1, padx=5)

# Task list
task_list = tk.Listbox(root, width=80, height=10,
                       bg='#F5E1FF', font=('Roboto', 10))
task_list.pack(pady=10)
task_list.bind('<<ListboxSelect>>', select_task)

display_tasks()
check_deadlines()

root.mainloop()

conn.close()
