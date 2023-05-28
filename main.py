import tkinter as tk
from tkinter import simpledialog, messagebox
from task_manager import TaskManager
from database import Database

db = Database()
task_manager = TaskManager(db)

def add_task():
    task = task_entry.get()
    if task:
        task_manager.add_task(task)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
    task_entry.delete(0, tk.END)

def delete_task():
    task = task_list.get(tk.ANCHOR)
    if task != "":
        task_manager.delete_task(task)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task.")

def edit_task():
    task = task_list.get(tk.ANCHOR)
    if task != "":
        new_task = simpledialog.askstring("Edit task", f"Edit '{task}'")
        if new_task is not None and new_task != "":
            task_manager.edit_task(task, new_task)
            update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task.")

def update_task_list():
    tasks = task_manager.get_tasks()
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

root = tk.Tk()

task_entry = tk.Entry(root)
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

task_list = tk.Listbox(root)
task_list.pack()

update_task_list()

root.mainloop()
