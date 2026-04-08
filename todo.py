import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)   # ✅ fixed indentation
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(tk.END, "✔ " + task)
    except:
        messagebox.showwarning("Warning", "Please select a task!")

title = tk.Label(root, text="To-Do List", font=("Arial", 20))
title.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=10)

done_btn = tk.Button(root, text="Mark as Done", command=mark_done)
done_btn.pack(pady=5)

del_btn = tk.Button(root, text="Delete Task", command=delete_task)
del_btn.pack(pady=5)

root.mainloop()