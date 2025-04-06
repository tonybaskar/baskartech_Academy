import tkinter as tk
from tkinter import messagebox # import math import datetime import os

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def remove_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove!")

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")
root.configure(bg="lightyellow")

# Entry field to add tasks
entry = tk.Entry(root, font=("Poppins", 12))
entry.pack(pady=10)

# Add button
add_btn = tk.Button(root, text="Add Task", command=add_task, bg="lightblue", font=("Poppins", 10))
add_btn.pack(pady=5)

# Listbox to show tasks
listbox = tk.Listbox(root, font=("Poppins", 12), width=30, height=10)
listbox.pack(pady=10)

# Remove button
remove_btn = tk.Button(root, text="Remove Task", command=remove_task, bg="lightcoral", font=("Poppins", 10))
remove_btn.pack(pady=5)

# Run the GUI app
root.mainloop()