import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import subprocess
import os

def create_database_if_not_exists():
    if not os.path.exists('users.db'):
        subprocess.run(["python", "create_table.py"])
        messagebox.showinfo('Success', 'Database table created.')

def save_to_database():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()

    if first_name and last_name:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()


        try:
            cursor.execute('INSERT INTO users (first_name, last_name) VALUES (?, ?)', (first_name, last_name))
            conn.commit()
            messagebox.showinfo('Success', 'User information saved.')
            display_records()
        except sqlite3.Error as e:
            conn.rollback()
            messagebox.showerror('Error', f'An error occurred: {e}')

        conn.close()
    else:
        messagebox.showwarning('Внимание', 'Please enter both first name and last name.')

def display_records():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()

    conn.close()

    for row in tree.get_children():
        tree.delete(row)

    for record in records:
        tree.insert("", "end", values=record)

app = tk.Tk()
app.title('User Registration')

label_first_name = tk.Label(app, text='First Name:')
label_last_name = tk.Label(app, text='Last Name:')
entry_first_name = tk.Entry(app)
entry_last_name = tk.Entry(app)
button_save = tk.Button(app, text='Save', command=save_to_database)
button_display = tk.Button(app, text='Display Records', command=display_records)
button_create_db = tk.Button(app, text='Create Database', command=create_database_if_not_exists)

label_first_name.pack()
entry_first_name.pack()
label_last_name.pack()
entry_last_name.pack()
button_save.pack()
button_display.pack()
button_create_db.pack()

tree = ttk.Treeview(app, columns=("ID", "First Name", "Last Name"))
tree.heading("#1", text="ID")
tree.heading("#2", text="First Name")
tree.heading("#3", text="Last Name")
tree.pack(padx=20, pady=20)

display_records()

app.mainloop()
